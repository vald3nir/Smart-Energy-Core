from src.database.MongoDB import MongoDB

# -----------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------

BACKUP_FOLDER = "src/database/backup/"

USERS_CSV = f"{BACKUP_FOLDER}users.csv"
TIME_SERIES_CSV = f"{BACKUP_FOLDER}timeseries.csv"

# -----------------------------------------------------------------------
# Databases
# -----------------------------------------------------------------------

userDB = MongoDB("users")
timeseriesDB = MongoDB("timeseries")
