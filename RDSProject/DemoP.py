import uuid, hashlib, mysql.connector, os

# SQLpassword = os.environ.get('databasePW')
# print(SQLpassword)



con = mysql.connector.connect(
  host="#hostname",
  user="root",
  password="#password",
  database="#DBName"
)

cur = con.cursor()

# cur.execute("SHOW DATABASES")
# db = cur.fetchall()
# print(db)

def getInfoAddDB():
    username = input("Enter uname: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    sql = f"""INSERT INTO `users` VALUES('{username}', '{password}','{email}')"""
    cur.execute(sql)
    con.commit()

getInfoAddDB()

def getDBInfo():
      sql = """SELECT * FROM users"""
      cur.execute(sql)
      output = cur.fetchall()
      print(output)

getDBInfo()

def getPasswordFromDB():

  usernameAttempt = input("What is your username? ")

  passwordAttempt = input("What is your password: ")

  sql = f"""SELECT password FROM users WHERE username='{usernameAttempt}'"""

  cur.execute(sql)

  storedDBpassword = cur.fetchone()[0]

  # print(storedDBpassword)

  if passwordAttempt == storedDBpassword:

    print('That was the same one')

  else:

    print('sorry wrong password')

getPasswordFromDB()

