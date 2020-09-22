import sys

def encrypt(arg, key):
    codes = []
    code = ""
    for txt in arg:
        for char in txt:
            if ord(char) > 122 - key:
                code += chr(ord(char) + key - 26)
            elif ord(char) > 90 - key:
                code += chr(ord(char) + key - 26)
            else:
                code += chr(ord(char) + key)
    
        codes.append(code)
        code =""
    return codes

def decrypt(arg, key):
    codes =[]
    code = ""
    for txt in arg:
        for char in txt:
            if ord(char) > 97 - key:
                code += chr(ord(char) - key +26)
            elif ord(char) > 65 - key:
                code += chr(ord(char) - key +26 )
            else:
                code += chr(ord(char) - key)
        codes.append(code)
        code = ""
    return codes


args = sys.argv[1:]
unique_arg = []
[unique_arg.append(arg) for arg in args if arg not in unique_arg]

key = int(input('Enter a key to encrypt \n'))
code = encrypt(unique_arg, key)
print(code)
print(decrypt(code, key))
