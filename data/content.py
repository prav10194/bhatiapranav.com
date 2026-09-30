"""All site content in one place. Edit here, not in the templates."""

# --- the line that changes most often -------------------------------------
NOW = (
    "two-minute tutor — a local adaptive coding tutor on flask + langchain + "
    "ollama. milestone 1/9. and kata, a calm ios habit tracker, heading to "
    "testflight."
)

INTRO_LEAD = (
    "i'm a senior software engineer at ibm. i build enterprise web platforms "
    "in typescript, react and java, and i live somewhere between a terminal "
    "and a ci pipeline."
)

INTRO_SUB = (
    "nine years in. currently teaching myself local-first ai — flask, "
    "langchain, ollama — and shipping small apps in the open as i go."
)

# --- projects --------------------------------------------------------------
# status: shipping | maintained | archived
PROJECTS = [
    {
        "name": "kata",
        "url": "https://github.com/prav10194",
        "blurb": (
            "a calm ios habit tracker. goals come in gentle chunks (2k steps "
            "at a time, not 10k), and instead of blocking apps it shows you "
            "time on reddit versus time on kindle. named for the japanese 型 "
            "— practiced form."
        ),
        "short": "an ios habit tracker with gentle, chunked goals and screen-time awareness instead of app blocking",
        "meta": ["swift · swiftui", "2026"],
        "status": "shipping",
        "featured": True,
    },
    {
        "name": "two-minute tutor",
        "url": "https://github.com/prav10194",
        "blurb": (
            "a local-first adaptive coding tutor. turns my own notes and code "
            "into two-minute exercises, remembers what i got wrong, and cites "
            "the source it used. flask, langchain, ollama — nothing leaves "
            "the machine."
        ),
        "short": "turns my own notes into two-minute coding exercises, entirely on a local model",
        "meta": ["python · flask", "milestone 1/9"],
        "status": "shipping",
        "featured": True,
    },
    {
        "name": "nltk-dictionary",
        "url": "https://github.com/prav10194/nltk-dictionary",
        "blurb": (
            "copy a word while reading an ebook on your pc; a desktop "
            "notification shows its meaning, synonyms and antonyms. "
            "nltk + wordnet."
        ),
        "short": "copy a word in any ebook → meaning, synonyms, antonyms as a desktop notification",
        "meta": ["python · 25★", "2016"],
        "status": "maintained",
        "featured": True,
    },
    {
        "name": "tekton-pipeline-example",
        "url": "https://github.com/prav10194/tekton-pipeline-example",
        "blurb": "a working tekton ci/cd pipeline on openshift",
        "short": "a working tekton ci/cd pipeline on openshift",
        "meta": ["shell · 2★", "2022"],
        "status": "archived",
        "featured": False,
    },
    {
        "name": "mac-cron-app-pyqt5",
        "url": "https://github.com/prav10194/mac-cron-app-pyqt5",
        "blurb": "a desktop ui for writing cron jobs on macos",
        "short": "a desktop ui for writing cron jobs on macos",
        "meta": ["python · pyqt5", "2021"],
        "status": "archived",
        "featured": False,
    },
    {
        "name": "nlp-project",
        "url": "https://github.com/prav10194/NLP-Project",
        "blurb": "semantic matching over 50 faqs, stanford corenlp behind a flask api",
        "short": "semantic matching over 50 faqs, stanford corenlp behind a flask api",
        "meta": ["python", "2018"],
        "status": "archived",
        "featured": False,
    },
    {
        "name": "nltk-text-summarizer",
        "url": "https://github.com/prav10194/nltk-text-summarizer",
        "blurb": "copy an article, get an extractive summary back",
        "short": "copy an article, get an extractive summary back",
        "meta": ["python", "2016"],
        "status": "archived",
        "featured": False,
    },
]

STATUS_ORDER = ["shipping", "maintained", "archived"]

# --- writing ---------------------------------------------------------------
WRITING = [
    {"date": "2025-09-09", "title": "postmessage in salesforce omniscript",
     "url": "https://prav10194.medium.com/postmessage-in-salesforce-omniscript-983eed0452a0"},
    {"date": "2025-07-19", "title": "using a data mapper extract in omniscript with a dynamic filter",
     "url": "https://prav10194.medium.com/using-a-data-mapper-extract-in-omniscript-with-a-dynamic-filter-fc59a463e0a3"},
    {"date": "2025-07-17", "title": "omniscript: set values for a child key within a json object",
     "url": "https://prav10194.medium.com/omniscript-using-set-values-for-child-key-within-a-json-object-d47032ad830e"},
    {"date": "2024-10-05", "title": "#684 redundant connections",
     "url": "https://prav10194.medium.com/lt-684-redundant-connections-04d3e53152a7", "series": "graph problems"},
    {"date": "2024-10-01", "title": "#127 word ladder",
     "url": "https://prav10194.medium.com/lt-127-word-ladder-205b11485f22", "series": "graph problems"},
    {"date": "2024-09-29", "title": "#261 graph valid tree",
     "url": "https://prav10194.medium.com/lt-261-graph-valid-tree-c6f592c0535e", "series": "graph problems"},
    {"date": "2024-09-27", "title": "#130 surrounded regions",
     "url": "https://prav10194.medium.com/lt-130-surrounded-regions-dfcd99bafd54", "series": "graph problems"},
    {"date": "2024-09-25", "title": "#417 pacific atlantic water flow",
     "url": "https://prav10194.medium.com/lt-417-pacific-atlantic-water-flow-b29299315135", "series": "graph problems"},
    {"date": "2024-09-24", "title": "#994 rotting oranges",
     "url": "https://prav10194.medium.com/lt-994-rotting-oranges-92534c00f95d", "series": "graph problems"},
    {"date": "2024-09-21", "title": "#286 walls and gates",
     "url": "https://prav10194.medium.com/lt-286-walls-and-gates-b59f2dbf0054", "series": "graph problems"},
]

MEDIUM_URL = "https://prav10194.medium.com"

# --- about -----------------------------------------------------------------
ABOUT_LEAD = (
    "i started in conversational ai — a watson chatbot for a national grocer "
    "that had to work the same on the web, in an app, on alexa and on google "
    "home. then three years in london doing secdevops on openshift, where "
    "\"it works on my machine\" stopped being an acceptable sentence. since "
    "2022 i've been back in dallas building large public-sector web platforms."
)

ABOUT_SUB = (
    "the 2018 chatbot work is why the current llm work feels like a return, "
    "not a new field. i'm learning it local-first on purpose — a model on my "
    "own laptop, my own notes as the corpus — because that's the version that "
    "respects the data."
)

TIMELINE = [
    {"years": "2022 —", "current": True,
     "title": "senior software engineer, ibm — dallas.",
     "text": "enterprise web platforms in typescript, react and java; agentic ai pilots for public-sector intake."},
    {"years": "2019 – 22",
     "title": "secdevops engineer, ibm uk — london.",
     "text": "500+ deployments on red hat openshift; security tooling embedded into ci/cd for a uk bank's engineering teams."},
    {"years": "2017 – 19",
     "title": "full stack developer, ibm — dallas.",
     "text": "watson nlp chatbot across web, mobile, alexa, google home and messenger; react + node + cloudant behind it. presented at nrf in new york."},
    {"years": "2016 – 18",
     "title": "ms computer science, ut dallas.",
     "text": "nlp coursework produced nlp-project."},
    {"years": "2014", "muted": True,
     "title": "first commit on github.",
     "text": "co-authored two undergraduate papers, on binrank search and decision-tree classifiers."},
]

HACKATHONS = [
    {"year": "2026", "name": "ibm watsonx challenge — ask eka",
     "text": "one chat box that answers questions across jira, confluence and github, and can act on them: open an issue, draft a page, cut a branch. a tool-calling llm over a retrieval layer exposed as an mcp server, fastapi behind it, deployed on openshift. demoed."},
    {"year": "2026", "name": "ibm bob-a-thon — incisight",
     "text": "point it at a salesforce org and it reads the debug logs nobody wants to read: severity, root cause, the file at fault, and a proposed fix. an agent applies the fix, validates it against the tooling api, deploys it, and posts to slack. turns a 30-minute-to-two-hour diagnosis into minutes. demoed."},
]

CERTIFICATIONS = (
    "aws solutions architect (associate) · aws cloud practitioner · "
    "salesforce platform developer · salesforce mulesoft developer · "
    "salesforce ai associate · salesforce ux designer · "
    "microsoft power platform developer associate"
)

EDUCATION = "ms computer science, university of texas at dallas"

# --- lab -------------------------------------------------------------------
LAB = [
    {"name": "system design", "status": "in progress",
     "text": "this site is four html files. i then gave it a message bus, a cache, a load balancer and a monitoring stack, one layer at a time, to learn what each one is actually for — and measured what each one cost. layer 0 of 6.",
     "url": None},
]

# --- identity --------------------------------------------------------------
EMAIL = "pranav@bhatiapranav.com"
LINKS = [
    {"label": "github", "url": "https://github.com/prav10194"},
    {"label": "linkedin", "url": "https://linkedin.com/in/pranav-bhatia"},
    {"label": "medium", "url": MEDIUM_URL},
]
LOCATION = "dallas, tx"
YEAR = 2026
