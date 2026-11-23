---
title: What BM25 actually computes
date: 2026-11-23
summary: Three numbers multiplied together, worked by hand on five documents — and the two places the arithmetic quietly stops being what you think it is.
---

I have quoted the BM25 formula in interviews without being able to say why
there is a `2.2` sitting in front of it. This is me fixing that. The five
documents below are invented so the arithmetic stays readable. The numbers
pulled from a real cluster are labelled as measured.

## Five documents, one shard

```diagram the entire corpus
D1  "red hat"             →  [red, hat]                dl = 2
D2  "red hat pro"         →  [red, hat, pro]           dl = 3
D3  "red"                 →  [red]                     dl = 1
D4  "blue hat"            →  [blue, hat]               dl = 2
D5  "hat rack hat sale"   →  [hat, rack, hat, sale]    dl = 4

N     = 5                        documents with the field
avgdl = (2+3+1+2+4) / 5 = 2.4    mean field length
```

`dl` is the field's length in tokens. `N` and `avgdl` are properties of the
whole index, not of any one document. Hold on to that — it comes back at the
end and it is where most of the surprises live.

## The formula

```text the whole thing
score = boost × idf × tf

  boost = k1 + 1 = 2.2

  idf = ln( 1 + (N - n + 0.5) / (n + 0.5) )

                      f
  tf = ─────────────────────────────────
       f + k1 × (1 - b + b × dl/avgdl)

  k1 = 1.2     b = 0.75
```

Three inputs vary per query and per document: `n`, how many documents hold the
term; `f`, how often it appears in this one; `dl`, how long this field is.

## idf is computed once

`hat` is in D1, D2, D4 and D5, so `n = 4`.

```text substituting
(N - n + 0.5) / (n + 0.5)
  = (5 - 4 + 0.5) / (4 + 0.5)
  = 1.5 / 4.5
  = 0.333333

idf = ln(1 + 0.333333) = ln(4/3) = 0.287682
```

One number, used by every matching document. It says nothing about any
individual document — only how unusual the word is across the index.

```warn the rounding trap
`ln(1.33)` is `0.285179`. `ln(4/3)` is `0.287682`. Truncating at two decimal
places costs 0.0025 in the idf and moves a score in the third decimal. Carry
divisions at full precision and round at the end — if your hand-check nearly
matches an explain, suspect your arithmetic before the scorer's.
```

## tf is computed per document

```text D1 — "red hat", f=1, dl=2
1 - b + b × dl/avgdl
  = 1 - 0.75 + 0.75 × (2 / 2.4)
  = 0.25 + 0.625
  = 0.875                        ← the length factor

k1 × 0.875 = 1.05

tf = 1 / (1 + 1.05) = 0.487805
```

```text D5 — "hat rack hat sale", f=2, dl=4
0.25 + 0.75 × (4 / 2.4) = 1.5
1.2 × 1.5 = 1.8

tf = 2 / (2 + 1.8) = 0.526316
```

Notice `f` appears twice — numerator and denominator. That is the whole
mechanism of saturation, and it is why the second occurrence of a word is
worth far more than the twentieth.

## Multiply

```chart scores for query: hat
D5  hat rack hat sale  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  0.3331
D1  red hat            ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇    0.3087
D4  blue hat           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇    0.3087
D2  red hat pro        ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇         0.2610
```

D5 wins while being the longest document — two occurrences outweigh the length
penalty. D1 and D4 tie *exactly*, because `f`, `dl` and `idf` all match. D2
loses to D1 on a single extra token.

## A rarer word changes everything

`red` is in three documents instead of four. One fewer.

```text
(5 - 3 + 0.5) / 3.5 = 0.714286
idf = ln(1.714286) = 0.538997
```

```key nearly double
0.538997
one fewer document holding the term, and the idf almost doubles
```

Every `red` score beats every `hat` score. D3, which is the single word
"red", scores 0.707936 — more than twice D2's `hat` score. Rarity dominates,
and it dominates non-linearly.

```chart idf as a term becomes common, N = 10000
in  0.1% of docs  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  6.8591
in    1% of docs  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇            4.6003
in    5% of docs  ▇▇▇▇▇▇▇▇▇▇▇▇▇                   2.9948
in   10% of docs  ▇▇▇▇▇▇▇▇▇▇                      2.3022
in   25% of docs  ▇▇▇▇▇▇                          1.3862
in   50% of docs  ▇▇▇                             0.6931
in   75% of docs  ▇                               0.2877
in   90% of docs                                  0.1054
in   99% of docs                                  0.0101
```

A term in 1% of documents carries 450 times the weight of one in 99%. This is
why keyword search degrades in a specialised corpus: in a dairy catalogue the
word "milk" is in nearly everything, its idf collapses toward zero, and
ranking quietly falls back onto field length alone.

## Saturation, and the 2.2

```chart repeating a word, dl = 4
f = 1   ▇▇▇▇▇▇▇▇▇▇▇▇▇                       0.2260
f = 2   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                0.3331
f = 3   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇             0.3956
f = 4   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇          0.4365
f = 6   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇       0.4868
f = 10  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇     0.5364
f = 20  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  0.5806
```

Twenty occurrences is worth 2.6 times one occurrence, not twenty times. That
curve is `k1`, and it is the main thing BM25 added over TF-IDF — it kills
keyword stuffing by construction rather than by rule.

So what is the `2.2`? It is `k1 + 1`, and it exists to put a number on the
ordinary case. When a word appears once in a field of exactly average length:

```text
dl = avgdl  →  length factor = 1
tf = 1 / (1 + 1.2) = 0.454545
2.2 × 0.454545 = 1.000000
```

```key the anchor
1.0
one occurrence, average length — the baseline everything else is measured against
```

```note it is not your boost
In an `_explain` response this constant is labelled `boost`, which sends people
hunting through configs for a boost nobody set. It is `k1 + 1`. If you *do* add
`"boost": 2` to the clause, the line reads `4.4`.
```

## Length, on its own

```chart one occurrence, varying field length
dl = 1   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  0.3779
dl = 2   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇        0.3087
dl = 3   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇             0.2610
dl = 4   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                0.2260
dl = 6   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                    0.1783
dl = 8   ▇▇▇▇▇▇▇▇▇▇▇▇▇                       0.1472
```

`b = 0.75` controls how steep that is. At `b = 0` the bars are flat and length
is ignored entirely. At `b = 1` the penalty is at full strength.

## Where dl actually comes from

This is the first place the arithmetic stops being what it looks like.

At search time the original text is gone — the inverted index holds
term-to-documents, not a countable sequence of words. So the length is measured
at index time and stored as a **norm**: one byte, per document, per field.

One byte is 256 values for a field that might hold three tokens or fifty
thousand, so the encoding is deliberately uneven. Short lengths are exact.
Long ones get bucketed.

```console measuring it
$ # index documents of known length, then read the explain
$ GET norms-test/_search { "explain": true, ... }

real len    reported dl    label in the explain
   2             2         "dl, length of field"
  11            11         "dl, length of field"
  40            40         "dl, length of field (approximate)"
  41            40         "dl, length of field (approximate)"
 100            96         "dl, length of field (approximate)"
 101            96         "dl, length of field (approximate)"
```

```measured
41 tokens reports as 40. Both 100 and 101 report as 96 — two documents of
genuinely different length became identical to the scorer, because their norm
bytes are the same. Elasticsearch even tells you: the description string
changes to **(approximate)** once the value is a decoded bucket rather than a
count.
```

The practical consequences are small but worth knowing. A `keyword` field has
no norms at all by default, so `dl` is a placeholder `1` for every document —
which is why a `term` query on a keyword field returns the same score for every
hit on a shard, and why it belongs in a `filter` where scoring is skipped
entirely. And dropping norms on a field is a one-way door: `b` is applied at
search time so you can change it freely, but the norm itself is data, and
removing it means a reindex to get it back.

## Where N and avgdl actually come from

The second place, and the one that bites hardest.

**Every statistic in the formula is computed per shard, not per index.** Each
shard scores its own documents from its own `N`, its own `n`, its own `avgdl`,
and the coordinating node merges the ranked lists afterward.

I watched this wreck a test. Eight documents, lengths from 2 to 101 tokens,
one term in each — and the index had six shards:

```chart scores by document length, 8 docs across 6 shards
len   3  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  0.2966
len  41  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇   0.2906
len   2  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇     0.2877
len  40  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇            0.2215
len  10  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                0.1859
len  11  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                0.1788
len 101  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                  0.1588
len 100  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇                    0.1347
```

A 41-token document nearly beat a 2-token one. Nothing is broken — BM25 behaved
correctly on each shard. But with eight documents spread one or two per shard,
`avgdl` ranged from 2.0 to 70.5 depending on where a document landed. The
41-token document was *alone* on its shard, so it was average length by
definition and took almost no penalty.

```warn this is a sharding problem wearing a scoring costume
The instinct is to reach for `k1` and `b`. The actual fix is fewer shards. At
production volumes shard statistics converge and the effect disappears — it is
glaring precisely in the small test index where people first meet it.
`search_type=dfs_query_then_fetch` gathers global statistics first and makes it
go away, at the cost of an extra round trip.
```

## What I would keep

```text six lines
score = boost × idf × tf

idf   rarer term → higher, non-linearly
tf    more occurrences → higher, with diminishing returns (k1 = 1.2)
      longer field → lower (b = 0.75)
boost = k1 + 1 = 2.2, anchoring an ordinary match at 1.0

N, n and avgdl are per shard
```

Nobody is going to ask you to compute this by hand. What gets asked is which
direction things move — double the term frequency, double the field length,
make the term ten times more common — and the arithmetic is what makes those
answers instant rather than hedged.

The one place it genuinely earns its keep is sanity-checking. If a client's
explain output shows a top-level value that is not `boost × idf × tf`, there is
something else in play: a `function_score` multiplier, a clause boost, a custom
similarity. Spotting that needs mental arithmetic to one decimal place, not a
calculator.

## Check yourself

- Two identical products score differently. Name three possible causes.
- Why does `f` appear in both the numerator and the denominator of `tf`?
- A `term` query on a `keyword` field returns the same score for every hit.
  Why, and where should that query have gone instead?
- You set `b = 0`. What is now deciding the ranking?
