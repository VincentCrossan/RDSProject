import mysql.connector, os

# print(os.environ)
SQLpassword = os.environ.get('dbPassword')
 
# con = mysql.connector.connect(
#   host="127.0.0.1",
#   port="3306",
#   user="root",
#   password=f"{SQLpassword}",
#   database = 'testPython'
# )

# cur = con.cursor()

# try:
#     dropDB = """DROP DATABASE IF EXISTS `testPython`"""
#     cur.execute(dropDB)
#     createDb = """CREATE DATABASE `testPython`"""
#     cur.execute(createDb)
#     con.commit()
# except:
#     print('error')
# else:
#     print('Created')




# cur.execute("SHOW DATABASES")
# db = cur.fetchall()
# print(db)


con = mysql.connector.connect(
  host="#hostname",
  port="3306",
  user="root",
  password=f"{SQLpassword}",
  database = '#DBName'
)
cur = con.cursor()

createTable = """CREATE TABLE IF NOT EXISTS `users` (
    `username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`username`)
);"""

cur.execute(createTable)
con.commit()
# except:
#     print('error')


