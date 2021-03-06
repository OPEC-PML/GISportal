DEBUG = True
DEBUG_WITH_APTANA = False

JSON_SORT_KEYS = False

SECRET_KEY = 'p7i0-22@0eheas^kzw3=1qfug_x+5)5)8u4v=2iyiwwx1eh)37'

#OPENID_FOLDER = '/users/rsg/olcl/scratch/portal_opec/html/cache/openID'
OPENID_FOLDER = '/etc/httpd/sites/portal.marineopec.eu/openID'
DATABASE_URI = 'sqlite:///' + OPENID_FOLDER + '/user_storage.db'


LOG_LEVEL = "DEBUG"
# This path needs changing according to local server configuration
# Leave as empty if you want the log to be in the same place as the .wsgi
LOG_PATH = ''

# The error level of logging into the database
# E for errors only or W for warnings too
ERROR_LEVEL = "W"


# section to define root folder for markdown metadata files
#MARKDOWN_ROOT = "/users/rsg/olcl/scratch/portal_opec/markdown"
MARKDOWN_ROOT = "/etc/httpd/sites/portal.marineopec.eu/markdown"

MARKDOWN_DIRS = ['provider', 'indicator', 'contact', 'model_used']
