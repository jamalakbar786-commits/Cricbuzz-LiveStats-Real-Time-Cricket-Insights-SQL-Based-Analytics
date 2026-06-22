from urllib.parse import quote_plus
from sqlalchemy import create_engine

USERNAME = "root"
PASSWORD = quote_plus("@Jamal1995")
HOST = "localhost"
DATABASE = "cricbuzz_live_stats"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
)