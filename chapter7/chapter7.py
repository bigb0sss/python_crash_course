#!/usr/bin/python3

prompt = "\n[INFO] Type something and I will repeat it back to you "
prompt+= "(Enter 'quit' to end the program): " 

message = ""

while message != "quit":

    message = input(prompt)
    print(message)