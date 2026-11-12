---
title: what an embedding actually is
date: 2026-11-12
summary: 384 numbers, where they come from, and why both chunking and normalising fall out of a single averaging step.
---

i am building a retrieval system over incident reports, and i kept using the
word "embedding" without being able to say what one is. this is me fixing that.
the toy numbers below are invented to make the arithmetic readable. the two
measured numbers are labelled as measured.

## the problem keyword search cannot solve

at 3am someone types *"pods keep restarting, out of memory"*. the incident
already written up in the corpus says *"latency climbs over hours and pods
restart on OOM"*. same problem. almost no shared words. `Ctrl+F` returns
nothing.

i measured this on my laptop with `all-MiniLM-L6-v2`:

| compared | score |
| --- | --- |
| "pods restarting with OOMKilled" vs "container killed for using too much memory" | 0.452 |
| "pods restarting with OOMKilled" vs "TLS certificate expired" | 0.055 |

measured, not invented. the first pair shares no words at all and still scores
eight times higher. that gap is the entire basis of semantic search, and
everything below is the explanation of where it comes from.

## the model returns a position, not a score

feed text to the model and you get back a fixed list of numbers. for
`all-MiniLM-L6-v2` it is always **384 numbers**, whether the input is three
words or three hundred.

those numbers are coordinates. text with similar meaning lands at nearby
coordinates. the individual values mean nothing on their own, and there is no
"memory dimension" to go looking for.

what matters is **position in the list, not the size of a number**. invented
example, shrunk to four slots so it fits:

| slot | query | doc a |
| --- | --- | --- |
| 1 containers | 0.40 | 0.60 |
| 2 crash | 0.60 | 0.75 |
| 3 memory | 0.70 | 0.10 |
| 4 paperwork | 0.00 | 0.05 |

doc a's 0.75 and the query's 0.70 are nearly equal, and that means nothing:
they sit in different slots. you compare slot 3 to slot 3. doc a's memory slot
is 0.10, so doc a is a crash document that barely mentions memory. this tripped
me up for a while.

## how the text becomes those numbers

five steps, in order.

```
text
 │  1. split into sub-word tokens
 ▼
["pods", "restart", "on", "oo", "##m"]
 │  2. look up a starting vector per token (context-blind)
 ▼
one vector each
 │  3. six transformer layers: every token reads every other token
 ▼
one context-aware vector each
 │  4. average them
 ▼
one vector for the whole text
 │  5. scale it to length 1
 ▼
384 numbers
```

step 3 is where meaning appears. the word `restart` starts identical whether
the sentence is about a crashing pod or a laptop. after six passes of reading
its neighbours, the two have moved apart. the classic version of this is
"bank": same starting vector in "river bank" and "bank account", far apart by
the end.

## step 4 is literally an average, and that matters

i assumed pooling was something clever. it is not. invented numbers, four
slots, five tokens: add each column and divide by five.

```
col1: 0.4+0.6+0.1+0.3+0.2 = 1.6 / 5 = 0.32
col2: 0.8+0.5+0.1+0.6+0.5 = 2.5 / 5 = 0.50
col3: 0.6+0.7+0.2+0.9+0.8 = 3.2 / 5 = 0.64
col4: 0.1+0.1+0.0+0.2+0.1 = 0.5 / 5 = 0.10
```

that is the sentence embedding. a plain mean of its token vectors.

knowing this is worth more than it sounds, because the next two problems are
both consequences of it rather than separate topics to memorise.

## consequence one: chunking

take an incident write-up and bolt fifteen tokens of meeting notes onto it.
nothing is deleted. the incident is still there word for word. but the average
is now over twenty tokens instead of five, so the incident gets a quarter of
the vote.

| document | similarity to the query |
| --- | --- |
| incident alone | 0.99 |
| same incident plus meeting notes | 0.45 |

invented numbers, but the mechanism is exactly the averaging above. the answer
is still in the document and can no longer be found.

splitting the document fixes it. the incident paragraph gets a vector of its
own, where it is five tokens out of five again. chunking is not a best practice
someone invented. it is the direct consequence of step 4.

## consequence two: normalising

averaging more tokens also makes the resulting arrow shorter, because the token
vectors partly cancel each other out. that has nothing to do with relevance,
and it quietly rigs the ranking.

invented, but this is the case that made it click. doc a is nine words about a
deploy and never mentions memory. doc b is 150 words of an actual memory leak
investigation. query: *"pods keep restarting, out of memory"*.

| | raw score | after normalising |
| --- | --- | --- |
| doc a, 9 words, wrong topic | **0.76** | 0.78 |
| doc b, 150 words, right answer | 0.57 | **0.99** |

the raw ranking is wrong. doc a wins for being short. normalising rescales
every vector to length 1, keeping direction and discarding length, and the
right document comes back to the top.

so: normalising fixes unfair scaling, chunking fixes contaminated meaning.
different problems, and neither substitutes for the other.

## where the model's idea of "similar" comes from

nobody labelled millions of sentence pairs by hand. training used pairs humans
had already linked for free: a forum question and its accepted answer, a title
and its body, two questions flagged as duplicates.

```
   random text  <-- push apart
        |
   "why does my pod keep getting OOMKilled?"   *
                                               |  pull together
   "your container exceeded its memory limit"  *
        |
   random text  <-- push apart
```

embed all of them, nudge the true pair closer and the random ones further
apart, repeat about a billion times.

nobody ever told the model that OOMKilled means memory. it observed the two
phrases sitting on opposite sides of a question and answer pair, constantly.

the consequence worth keeping: the model's notion of "similar" is inherited
entirely from those pairs. it knows what internet text treats as related, and
nothing else.

## what it cannot do

three failures, all predictable from the above.

**exact identifiers.** every incident id tokenises into near-identical
meaningless fragments:

```
INC-1042  ->  ["inc", "##10", "##42"]
INC-1055  ->  ["inc", "##10", "##55"]
```

they pile into the same tiny region, indistinguishable. vector search has no
concept of equality, only nearest neighbours, so searching for `INC-1042`
returns an arbitrary handful of incidents. the fixes are metadata filtering and
hybrid keyword search, not a better model.

**negation.** "the service is restarting" and "the service is not restarting"
appear in near-identical contexts online and almost never as a labelled
contrastive pair, so nothing in training pushed them apart.

**internal names.** a service nobody outside a company ever wrote about has no
learned meaning. the tokeniser splits it, the recognisable fragment contributes
something vague, and the part that identifies it contributes noise.

## what tripped me up

i read a number in the wrong place. looking at a vector like
`[0.60, 0.75, 0.10, 0.05]` next to a query's `0.70`, i thought 0.75 being close
to 0.70 meant the documents matched. they are different slots. a vector is a
form with fixed rows, and you only ever compare a row to the same row.

i also assumed a lower similarity score meant the system got worse. my first
test corpus reused one symptom sentence per root cause, so 45 incidents shared
only 10 distinct descriptions. retrieval scored well by matching near
duplicates. after giving each incident its own phrasing, the distinct
descriptions went from 10 to 31 and the top score dropped from 0.588 to 0.561
(measured). the system did not change. the benchmark stopped being rigged.

## check yourself

- a 60 word incident and a 5,000 word post-mortem. how many numbers in each
  embedding, and what happens to most of the long one?
- why does normalising help, and what exactly is being thrown away?
- you need to find the incident whose id is `INC-1042`. why is a vector search
  the wrong tool, and what would you use instead?

## still unsure about

- how much a chunk size of 120 words actually costs me versus 200 or 400. i
  have a held out set of 15 incidents and no measurements yet.
- whether a model trained more on code and logs would beat `all-MiniLM-L6-v2`
  on incident text, or whether the difference disappears once reranking is in
  front of it.
- how reranking changes any of this, which is the next thing i am reading about.
