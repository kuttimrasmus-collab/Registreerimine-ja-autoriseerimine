import random
import string

existing_users = {
    "user1": "Password123!",
    "admin": "AdminPass!1",
    "testuser": "Test1234!"
}

def check_username_availability(username):
    return username not in existing_users

def generate_password():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for _ in range(12)])
    return psword

def validate_password(pw):
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in ".,:;!_*-+()/#¤%&" for c in pw)
    return has_upper and has_lower and has_digit and has_special

def user_defined_password():
    while True:
        pw = input("Sisesta parool: ")
        if validate_password(pw):
            print("Parool sobib.")
            return pw
        else:
            print("Parool peab sisaldama suur- ja väiketähte, numbrit ning erimärki.")

def register():
    username = input("Sisesta kasutajanimi: ")
    if not check_username_availability(username):
        print("Kasutajanimi on juba kasutuses.")
        return
    choice = input("Kas soovid automaatselt parooli genereerida? (jah/ei): ").lower()
    if choice == 'jah':
        password = generate_password()
        print(f"Genereeritud parool: {password}")
    else:
        password = user_defined_password()

    existing_users[username] = password
    print(f"Kasutaja {username} registreeriti edukalt!")

def login():
    username = input("Kasutajanimi: ")
    password = input("Parool: ")

    if username in existing_users and existing_users[username] == password:
        print("Sisselogimine õnnestus!")
    else:
        print("Vale kasutajanimi või parool.")
