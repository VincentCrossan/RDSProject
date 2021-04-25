import uuid, hashlib, mysql.connector, os

con = mysql.connector.connect(

  host="#hostname",

  user="root",

  password="#password",

  database="#DBName"

)

cur = con.cursor()

def hasher(password):   #The hash function used to hash a password
    salt = uuid.uuid4()
    salt = uuid.uuid4().hex

    hashedPassword = hashlib.sha256(salt.encode()+password.encode()).hexdigest()+":"+salt
    return hashedPassword


def verifyhash(passwordAttempt, dbStoredHashePass):         #Verifies the hash
    try:                                            #Prevents crash in instance of invalid stored hash
        password,salt=dbStoredHashePass.split(":")
    except:
        pass
    else:
        hashedPasswordAttempt = hashlib.sha256(salt.encode()+passwordAttempt.encode()).hexdigest()
        return hashedPasswordAttempt == password


def checkUnameUnique(username):

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

def signUp():

    isValid = False

    isFoundInDB = True

    while isValid == False and isFoundInDB == True:

        username = input("Enter uname: ") #add regex

        password = input("Enter password: ") #add regex

        email = input("Enter email: ") #add regex

        birthyear = input("Enter year: ")

        if username and password and email and birthyear:

            isValid = True

            sql = f"""SELECT username FROM users WHERE username='{username}'"""

            cur.execute(sql)

            result = cur.fetchone()

            if result:

                print('This already exists')
                print('perhaps try these variations:')

            else:

                passwordOut = hasher(password)

                isFoundInDB = False

                sql = f"""INSERT INTO `users` VALUES('{username}', '{passwordOut}', '{email}')"""

                cur.execute(sql)

                con.commit()

def login():
  loggedIn = False
  while loggedIn == False:
    usernameMatch = False
    while usernameMatch == False:

        usernameAttempt = input("What is your username? ")

        passwordAttempt = input("What is your password: ")

        sql = f"""SELECT password FROM users WHERE username='{usernameAttempt}'"""

        cur.execute(sql)

        try:
            storedDBpassword = cur.fetchone()[0]
            # print(storedDBpassword)
            verfified = verifyhash(passwordAttempt, storedDBpassword)
            usernameMatch = True
        except:
            print('This username is not in the database, please try again ')
        # print(storedDBpassword)

    if verfified:
        loggedIn = True
        print('Login Successful')

    else:

        print('sorry wrong password')


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
    



def main():
    #exit clause which determins when the main program ends
    print('Welcome to my program. \n')
    whatYouWant()

main()