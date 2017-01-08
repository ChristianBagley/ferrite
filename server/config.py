import os.path

BASE_DIR = os.path.dirname(__file__)

# DB_URL = 'sqlite:///' + os.path.join(BASE_DIR, "db.sqlite")
DB_URL = 'postgresql://scott:tiger@localhost:5432/mydatabase'

try:
    from local_config import * # NOQA
except ImportError:
    pass
