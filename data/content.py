"""All site content in one place. Edit here, not in the templates."""

# --- the line that changes most often -------------------------------------
NOW = (
    "two-minute tutor — a local adaptive coding tutor on flask + langchain + "
    "ollama. milestone 1/9. and kata, a calm ios habit tracker, heading to "
    "testflight."
)

INTRO_LEAD = (
    "i'm a technical architect at ibm, in austin. i build search and "
    "retrieval systems \u2014 elasticsearch, kibana, rag \u2014 inside large "
    "government and enterprise platforms."
)

INTRO_SUB = (
    "nine years advising clients across the us, uk and canada, in federal and "
    "state government, healthcare, financial services, retail and energy. i "
    "still write the code."
)

# the arc, for the home page
STORY_LEAD = (
    "i started in conversational ai \u2014 a watson chatbot for a national "
    "grocer that had to work the same on the web, in an app, on alexa and on "
    "google home. then three years in london doing secdevops on openshift, "
    "where \"it works on my machine\" stopped being an acceptable sentence. "
    "since 2022 i've been architecting large public-sector platforms, and "
    "lately that has meant search."
)

STORY_SUB = (
    "the 2018 chatbot work is why the current llm work feels like a return, "
    "not a new field. i'm learning it local-first on purpose \u2014 a model on "
    "my own laptop, my own notes as the corpus \u2014 because that's the "
    "version that respects the data."
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
    {"date": "2025-07-19", "title": "a data mapper extract in omniscript with a dynamic filter",
     "url": "https://prav10194.medium.com/using-a-data-mapper-extract-in-omniscript-with-a-dynamic-filter-fc59a463e0a3"},
    {"date": "2025-07-17", "title": "omniscript: set values for a child key within a json object",
     "url": "https://prav10194.medium.com/omniscript-using-set-values-for-child-key-within-a-json-object-d47032ad830e"},
    {"date": "2024-03-13", "title": "deleting a record type that chatter profiles still hold on to",
     "url": "https://prav10194.medium.com/delete-record-type-connected-to-chatter-profiles-b92865903b2f"},
    {"date": "2024-01-19", "title": "passing information from omniscript to a flexcard",
     "url": "https://prav10194.medium.com/passing-information-from-omniscript-to-flexcard-064097afe53a"},
    {"date": "2021-09-09", "title": "a python package that runs straight from the terminal",
     "url": "https://prav10194.medium.com/creating-a-python-package-that-can-run-directly-from-terminal-35933f3a61b3"},
    {"date": "2021-09-09", "title": "a custom lightning data table in lwc",
     "url": "https://prav10194.medium.com/creating-a-custom-lightning-data-table-in-lwc-517bc4637d8e"},
    {"date": "2021-08-19", "title": "setting up kubernetes with jenkins on red hat openshift",
     "url": "https://prav10194.medium.com/setting-up-kubernetes-with-jenkins-466c51713cc0"},
    {"date": "2021-06-30", "title": "connecting an omniscript with lwc",
     "url": "https://prav10194.medium.com/connecting-your-omniscript-with-lwc-1fd8374c5b15"},
    {"date": "2021-02-16", "title": "analysing a node project in sonarqube with tekton pipelines",
     "url": "https://prav10194.medium.com/analyzing-your-node-project-in-sonarqube-using-tekton-pipelines-on-ibm-cloud-bd006bf7cfa2"},
    {"date": "2019-05-06", "title": "watson assistant v2 \u2014 handling context variables",
     "url": "https://prav10194.medium.com/watson-assistant-v2-context-sharing-3ca18626ed0d"},
    {"date": "2018-09-10", "title": "keeping conversation context in an alexa skill",
     "url": "https://prav10194.medium.com/keep-conversation-context-in-alexa-skill-edd8ab8002fa"},
    {"date": "2017-12-29", "title": "integrating alexa with the watson weather service",
     "url": "https://prav10194.medium.com/integrating-alexa-with-watson-weather-service-18b482b2a637"},
]

# "cover" is a file in static/covers/ and always wins. Without one the page
# asks openlibrary for the jacket by isbn, and falls back to a blank block.
BOOKS = [
    {"title": "the big short", "author": "michael lewis", "meta": "2010",
     "status": "reading", "isbn": "9780393338829", "cover": "", "line": ""},
    {"title": "breasts and eggs", "author": "mieko kawakami",
     "meta": "tr. sam bett & david boyd", "status": "reading",
     "isbn": "9781609456702", "cover": "", "line": ""},
    {"title": "kafka on the shore", "author": "haruki murakami",
     "meta": "tr. philip gabriel", "status": "read",
     "isbn": "9781400079278", "cover": "", "line": ""},
    {"title": "what you are looking for is in the library",
     "author": "michiko aoyama", "meta": "tr. alison watts", "status": "read",
     "isbn": "9781804994139", "cover": "", "line": ""},
]

BOOK_STATUS_ORDER = ["reading", "read"]

MEDIUM_URL = "https://prav10194.medium.com"

# --- experience ------------------------------------------------------------
TIMELINE = [
    {"years": "2022 \u2014", "current": True,
     "title": "technical architect, ibm \u2014 austin.",
     "text": "retrieval-augmented incident diagnosis over application logs in elasticsearch; a state vehicle-registration platform moved off a platform-native event bus and onto kafka; fl wins, a florida workforce portal consolidating 42 programs into one intake flow. led four offshore engineers for two years."},
    {"years": "2019 \u2013 22",
     "title": "secdevops engineer, ibm uk \u2014 london.",
     "text": "the elastic stack monitoring 500+ containerised deployments across three enterprise clients, with react and node dashboards over the same signals; devsecops practices embedded into ci/cd with lloyds bank security and infosec."},
    {"years": "2017 \u2013 19",
     "title": "advisory it specialist, ibm \u2014 dallas.",
     "text": "watson nlp product search over a 10,000-sku catalogue for a national grocer, across web, mobile, alexa, google home and messenger; react + node + cloudant behind it. presented it at nrf in new york."},
    {"years": "2016 \u2013 18",
     "title": "ms computer science, ut dallas.",
     "text": "major in data science. nlp coursework produced nlp-project."},
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
    "aws solutions architect \u2013 associate \u00b7 aws cloud practitioner \u00b7 "
    "salesforce mulesoft developer \u00b7 salesforce omnistudio developer \u00b7 "
    "salesforce cpq specialist \u00b7 salesforce ai associate \u00b7 "
    "salesforce ux designer \u00b7 microsoft power platform developer associate"
)

EDUCATION = (
    "ms computer science, major in data science \u2014 university of texas at dallas"
)

# --- lab -------------------------------------------------------------------
LAB = [
    {"name": "system design", "status": "in progress",
     "text": "this site is four html files. i then gave it a message bus, a cache, a load balancer and a monitoring stack, one layer at a time, to learn what each one is actually for — and measured what each one cost. layer 0 of 6.",
     "url": None},
]

# --- identity --------------------------------------------------------------
# --- resume ----------------------------------------------------------------
# Drop the pdf in static/ and put its filename here to show the download link.
RESUME_PDF = ""

RESUME_LEAD = (
    "technical architect with nine years advising enterprise clients across "
    "the us, uk and canada \u2014 federal and state government, healthcare, "
    "financial services, retail and energy. i lead engagements from discovery "
    "through production rollout and client enablement, and stay hands-on."
)

SKILLS = [
    ("search & ai", "elasticsearch \u00b7 kibana \u00b7 retrieval-augmented generation \u00b7 nlp search \u00b7 log ingestion and alerting rules"),
    ("languages & data", "python \u00b7 flask \u00b7 javascript \u00b7 node \u00b7 sql server \u00b7 mongodb \u00b7 java"),
    ("cloud & devops", "aws \u00b7 linux \u00b7 docker \u00b7 kubernetes \u00b7 terraform \u00b7 ci/cd \u00b7 red hat openshift"),
    ("delivery", "discovery workshops \u00b7 solution architecture \u00b7 design and code review \u00b7 client enablement \u00b7 mentoring \u00b7 agile"),
]

EMAIL = "pranav.bhatia@hotmail.com"
LINKS = [
    {"label": "github", "url": "https://github.com/prav10194"},
    {"label": "linkedin", "url": "https://linkedin.com/in/pranav-bhatia"},
    {"label": "medium", "url": MEDIUM_URL},
]
LOCATION = "austin, tx"
YEAR = 2026
