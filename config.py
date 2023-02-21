from os import path

APP_DIR = path.dirname(path.dirname(path.realpath(__file__)))
SKIN_DIR = path.join(APP_DIR, "view")
TEMPLATES_DIR = path.join(SKIN_DIR, "templates")
STATIC_DIR = path.join(SKIN_DIR, "style")
LOGFILE = APP_DIR + "/vocprez.log"
CACHE_FILE = path.join(APP_DIR, "cache", "DATA.p")
CACHE_HOURS = 1
DEFAULT_LANGUAGE = "en"
SPARQL_QUERY_LIMIT = 2000  # Maximum number of results to return per SPARQL query
MAX_RETRIES = 2
RETRY_SLEEP_SECONDS = 10
SPARQL_TIMEOUT = 60
PORT = 5000

# Vocabulary data sources
#
# Here is the list of vocabulary sources that this instance uses. FILE, SPARQL, RVA & VOCBENCH are implemented already
# and are on by default (e.g. VOCBENCH = None) but other sources, such as GitHub can be added. To enable them, add a new
# like VocBench.XXX = None
class VocabSource:
    FILE = "FILE"
    SPARQL = "SPARQL"
    RVA = "RVA"
    VOCBENCH = "VOCBENCH"
    GITHUB = "GITHUB"


# BEGIN Instance Vars
SYSTEM_BASE_URI = "$SYSTEM_BASE_URI"
USE_SYSTEM_URIS = True
DEBUG = False
SPARQL_ENDPOINT = "$SPARQL_ENDPOINT"
SPARQL_USERNAME = $SPARQL_USERNAME
SPARQL_PASSWORD = $SPARQL_PASSWORD
SOURCE_NAME = "ga"
# END Instance Vars

DATA_SOURCES = {
    # example SPARQL source configured using variables in "Instance Vars" above
    SOURCE_NAME: {
        "source": VocabSource.SPARQL,
        "sparql_endpoint": SPARQL_ENDPOINT,
        "sparql_username": SPARQL_USERNAME,
        "sparql_password": SPARQL_PASSWORD,
    },
}

# BEGIN Vocabs list info
VOCS_TITLE = "GGIC Vocabularies"
# VOCS_URI = "http://www.geoscience.gov.au/data-standards/ggic-vocab-register"
VOCS_URI = "https://nonprod.ggic.vocabs.ga.gov.au/vocab/"
VOCS_DESC = "Vocabularies managed and published by Geoscience Australia on behalf of the Government Geoscience Information Committee (GGIC), within the Australian Geoscience Information Network (AusGIN)."
# END Vocabs list info
