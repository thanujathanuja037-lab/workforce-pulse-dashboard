import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Load CSV file
csv_file = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
df = pd.read_csv(csv_file)

print("Rows:", len(df))

# MySQL password
password = quote_plus("Mysql@24")

# Create MySQL connection
engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/workforce_pulse"
)

# Load data into MySQL
df.to_sql(
    "employees",
    con=engine,
    if_exists="replace",
    index=False
)

print("Loaded successfully")