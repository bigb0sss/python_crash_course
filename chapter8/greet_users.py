def greet_users(names):
    for i in names:
        msg = "Hello, " + i.title() + "!"
        print(msg)

usernames = [
    "brian",
    "dan",
    "margor",
]

greet_users(usernames)