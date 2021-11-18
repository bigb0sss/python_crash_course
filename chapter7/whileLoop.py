#!/usr/bin/python3

# Using flag
active = True

prompt = "\n[INFO] Type something and I will repeat it back to you "
prompt+= "(Enter 'quit' to end the program): " 

message = ""

while message != "quit":

    if message == 'quit':
        active = False
    else:
        message = input(prompt)
        print(message)