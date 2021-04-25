import hashlib
import uuid



password = "password1"
def hasher(password):   #The hash function used to hash a password
    salt = uuid.uuid4()
    print(salt)
    salt = uuid.uuid4().hex
    print(salt)

    hashedPassword = hashlib.sha256(salt.encode()+password.encode()).hexdigest()+":"+salt
    return hashedPassword


def main():
    passwordOut = hasher(password)
    print(passwordOut)

main()




def verifyhash(self, userpass, storedpass):         #Verifies the hash
    self.userpass = userpass
    try:                                            #Prevents crash in instance of invalid stored hash
        password,salt=storedpass.split(":")
    except:
        pass
    else:
        data = []
        data.append(password)
        data.append(hashlib.sha256(salt.encode()+self.userpass.encode()).hexdigest())
        return data[0]==data[1]
