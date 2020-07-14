from pyuser.db.database import Database
from pyuser.settings.config import TEST_DB_NAME

db_client = Database(db_name=TEST_DB_NAME)