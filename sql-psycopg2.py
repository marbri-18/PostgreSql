import psycopg2

# Connect to the Chinook database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print Results
for result in results:
    print(result)