import uuid, hashlib, mysql.connector, os

# SQLpassword = os.environ.get('dbPassword')

 

con = mysql.connector.connect(

  host="#hostname",

  user="root",

  password="#password",

  database="#DBName"

)

cur = con.cursor()

def checkUnameUniqe(username):

    isFoundInDB = True

    while isFoundInDB == True:

        sql = f"""SELECT username FROM users WHERE username='{username}'"""

        cur.execute(sql)

        result = cur.fetchone()

        if result:

            print('This already exists')

        else:

            isFoundInDB = False

    return isFoundInDB

def login():

    isValid = False

    addedToDb = False

    while isValid == False and addedToDb == False:

        username = input("Enter uname: ") #add regex

        password = input("Enter password: ") #add regex

        email = input("Enter email: ") #add regex

        if username and password and email:

            isValid = True

            isFoundInDB = checkUnameUniqe(username)

            if isFoundInDB == False:

                sql = f"""INSERT INTO `users` VALUES('{username}', '{password}', '{email}')"""

                cur.execute(sql)

                con.commit()

                addedToDb = True

def signUp():

    isValid = False

    isFoundInDB = True

    while isValid == False and isFoundInDB == True:

        username = input("Enter uname: ") #add regex

        password = input("Enter password: ") #add regex

        email = input("Enter email: ") #add regex

        if username and password and email:

            isValid = True

            sql = f"""SELECT username FROM users WHERE username='{username}'"""

            cur.execute(sql)

            result = cur.fetchone()

            if result:

                print('This already exists')

            else:

                isFoundInDB = False

                sql = f"""INSERT INTO `users` VALUES('{username}', '{password}', '{email}')"""

                cur.execute(sql)

                con.commit()

def whatYouWant():

    isValid = False

    while isValid == False:

        choice = int(input("Would you like to 1.login or 2.sign up? "))

        if choice == 1:

            isValid = True

            login()

        elif choice == 2:

            isValid = True

            signUp()

        else:

            print('Please choose 1 or 2')

whatYouWant()

    ##if choice ==1 run loginIn func, if choice == 2 run signUp func

def signUp():

    isValid = False

    isFoundInDB = True

    while isValid == False and isFoundInDB == True:

        username = input("Enter uname: ") #add regex

        password = input("Enter password: ") #add regex

        email = input("Enter email: ") #add regex

        if username and password and email:

            isValid = True

            sql = f"""SELECT username FROM users WHERE username='{username}'"""

            cur.execute(sql)

            result = cur.fetchone()

            if result:

                print('This already exists')

            else:

                isFoundInDB = False

                sql = f"""INSERT INTO `users` VALUES('{username}', '{password}', '{email}')"""

                cur.execute(sql)

                con.commit()

###########################################################################

##splitting up the functions

def checkUnameUniqe(username):

    isFoundInDB = True

    while isFoundInDB == True:

        sql = f"""SELECT username FROM users WHERE username='{username}'"""

        cur.execute(sql)

        result = cur.fetchone()

        if result:

            print('This already exists')

        else:

            isFoundInDB = False

    return isFoundInDB

def login():

    isValid = False

    addedToDb = False

    while isValid == False and addedToDb == False:

        username = input("Enter uname: ") #add regex

        password = input("Enter password: ") #add regex

        email = input("Enter email: ") #add regex

        if username and password and email:

            isValid = True

            isFoundInDB = checkUnameUniqe(username)

            if isFoundInDB == False:

                sql = f"""INSERT INTO `users` VALUES('{username}', '{password}', '{email}')"""

                cur.execute(sql)

                con.commit()

                addedToDb = True
###########################################################################

def signUpEasy():

    isValid = False

    while isValid == False:

        username = input("Enter uname: ") #add regex

        password = input("Enter password: ") #add regex

        email = input("Enter email: ") #add regex

        if username and password and email:

            isValid = True

            sql = f"""INSERT INTO `users` VALUES('{username}', '{password}', '{email}')"""

            cur.execute(sql)

            con.commit()

def login():

    isRightPassword = False

    while isRightPassword == False:

        username = input("What is your username? ")

        passwordAttempt = input("What is your password: ")

        sql = f"""SELECT password FROM users WHERE username='{username}'"""

        cur.execute(sql)

        storedDBpassword = cur.fetchone()[0]

        if passwordAttempt == storedDBpassword:

            print('That was the same one')

            isRightPassword = True

        else:

            print('sorry wrong password')