import mysql.connector
import time

# Database connection details
host = "localhost"
user = "root"
password = "nandhu01"
database = "test_db"

# Wait and try connecting
for i in range(10):
    try:
        conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        if conn.is_connected():
            print("Connected to MySQL successfully!")
            cursor = conn.cursor()

            # Create a table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100) UNIQUE
                )
            ''')
            print("Table 'users' created successfully.")

            # Insert a sample record
            cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")
            conn.commit()
            print("Sample user inserted successfully.")

            # Retrieve data
            cursor.execute("SELECT * FROM users")
            for row in cursor.fetchall():
                print(row)

            break
    except Exception as e:
        print(f"Connection failed: {e}")
        time.sleep(5)
else:
    print("Could not connect to MySQL.")

# Close connection
if conn.is_connected():
    conn.close()

