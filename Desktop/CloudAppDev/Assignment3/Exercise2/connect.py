import mysql.connector

cnx = mysql.connector.connect(
    user='root',  # or your username
    password='alihan11',  # replace with your root password
    host='34.159.126.90',  # replace with your Cloud SQL public IP
    database='sample_db'
)

cursor = cnx.cursor()
cursor.execute('SELECT * FROM users')

for row in cursor:
    print(row)

cursor.close()
cnx.close()
