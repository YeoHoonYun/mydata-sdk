# -*- coding: utf-8 -*-
from base64 import b64encode
import os
from uuid import uuid4

DEBUG = False

# Enable more detailed logging
SUPER_DEBUG = True

# Application URL prefix
## Only leading slash
APP_URL_PREFIX = "/account/api/v1.3"

# Logger
LOG_FORMATTER = '%(asctime)s - %(name)s in function %(funcName)s at line: %(lineno)s - %(levelname)s - %(message)s'
LOG_PATH = './logs/'
LOG_FILE = LOG_PATH + 'account.log'
LOG_TO_FILE = False
LOG_LEVEL = 'DEBUG'

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
# Flask-MySQLdb - http://flask-mysqldb.readthedocs.org/en/latest/
MYSQL_HOST = 'localhost'  # Name of host to connect to. Default: use the local host via a UNIX socket (where applicable)
MYSQL_USER = 'mydataaccount'  # User to authenticate as. Default: current effective user.
MYSQL_PASSWORD = 'wr8gabrA'  # Password to authenticate with. Default: no password.
MYSQL_DB = 'MyDataAccount'  # Database to use. Default: no default database.
MYSQL_PORT = 3306  # TCP port of MySQL server. Default: 3306.
#MYSQL_UNIX_SOCKET = ''  # Location of UNIX socket. Default: use default location or TCP for remote hosts.
#MYSQL_CONNECT_TIMEOUT = '10'  # Abort if connect is not completed within given number of seconds. Default: 10
#MYSQL_READ_DEFAULT_FILE = ''  # MySQL configuration file to read, see the MySQL documentation for mysql_options().
#MYSQL_USE_UNICODE = ''  # If True, CHAR and VARCHAR and TEXT columns are returned as Unicode strings, using the configured character set.
MYSQL_CHARSET = 'utf8'  # If present, the connection character set will be changed to this character set, if they are not equal. Default: utf-8
MYSQL_SQL_MODE = 'TRADITIONAL'  # If present, the session SQL mode will be set to the given string.
#MYSQL_CURSORCLASS = ''  # If present, the cursor class will be set to the given string.


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 1

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = str(os.urandom(24))

# Secret key for signing cookies
SECRET_KEY = str(os.urandom(24))

# SDK Api-Key
SDK_API_KEY = b64encode(str(uuid4()) + "-" + str(uuid4()))

# http://flask-restful-cn.readthedocs.org/en/0.3.5/reqparse.html#error-handling
BUNDLE_ERRORS = True

# Flask-Login
LOGIN_VIEW = "signin"  # https://flask-login.readthedocs.org/en/latest/#customizing-the-login-process
LOGIN_MESSAGE = "Authentication required"  # https://flask-login.readthedocs.org/en/latest/#customizing-the-login-process
SESSION_PROTECTION = "strong"  # https://flask-login.readthedocs.org/en/latest/#session-protection
# Optional cookie settings: https://flask-login.readthedocs.org/en/latest/#cookie-settings

# Default icon for Account
AVATAR = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQCAYAAACAvzbMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDoyOTlBNEQ2MTAwQjQxMUU1QjU1MEI0OEI1ODg3N0RFQyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDoyOTlBNEQ2MjAwQjQxMUU1QjU1MEI0OEI1ODg3N0RFQyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjI5OUE0RDVGMDBCNDExRTVCNTUwQjQ4QjU4ODc3REVDIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjI5OUE0RDYwMDBCNDExRTVCNTUwQjQ4QjU4ODc3REVDIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+s6INdgAAHL9JREFUeNrs3QmY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'
