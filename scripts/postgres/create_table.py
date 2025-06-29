import psycopg2

# Connect to your postgres database
conn = psycopg2.connect(
    dbname="mydatabase",
    user="postgres",
    password="",  # Replace with your actual password
    host="localhost"
)

cur = conn.cursor()

# Example: Create a simple table named 'example_table'
cur.execute("""
    CREATE TABLE IF NOT EXISTS example_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

conn.commit()
cur.close()
conn.close()

print("Table created successfully.")