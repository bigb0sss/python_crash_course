#!/usr/bin/python3

# Dictionaries

dictionary = { "color1" : "red",
               "color2" : "yellow",
               "color3" : "green"        
}

print(dictionary['color1'])
print(dictionary['color2'])
print(dictionary['color3'])

# Loop dictionaries
for key, value in dictionary.items():
    print(f"[INFO] key: {key}")
    print(f"[INFO] value: {value}")
