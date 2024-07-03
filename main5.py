import psycopg2

import psycopg2

database = 'homework3'
user = 'postgres'
host = 'localhost'
port = 5432
password = '0909'

conn = psycopg2.connect(database = database, user = user, host = host, port = port, password = password)
cur = conn.cursor()


select_students_query = ''' select * from lesson4.students; '''

cur.execute(select_students_query)
students = cur.fetchall()

for student in students:
    print(student)

# new comment    