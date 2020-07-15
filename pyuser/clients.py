from pyuser.db.database import Database
from pyuser.settings.config import DB_NAME

db_client = Database(db_name=DB_NAME)