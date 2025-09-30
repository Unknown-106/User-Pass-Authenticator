# AS Computer Science
# 18/9/2025
# Azhi Amin
# User-Pass Authenticator

import time

def userLogin():
    username = ""
    password = ""
    attempts = 0
    while username != "admin" or password != "passwd":
        attempts = checkAttempts(attempts)
        username = input("Username: ")
        password = input("Password: ")
        attempts += 1
        checkAdmin(username, password)

def checkAdmin(username, password):
    if username == "admin" and password == "passwd":
        print("\nAccess Granted")
    else:
        print("\nAccess Denied\nTry again\n")

def checkAttempts(attempts):
    if attempts >= 5:
        attempts = 0
        print("Too many login attempts. Please wait 1 minute before retrying.\n")
        time.sleep(60)
    return attempts

userLogin()
