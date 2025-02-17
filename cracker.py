import hashlib

passwords = {}

with open("passwords.txt", "r") as f:
    common_passwords = f.read().splitlines()


with open("hashed.txt", "r") as f:
    text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        passwords[username] = hash

for user, hash in passwords.items():
    print(user, hash)

for password in common_passwords:
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    for username, hash in passwords.items():
        if hashed_password == hash:
            print(f"HASH FOUND\n{username} : {password}")
