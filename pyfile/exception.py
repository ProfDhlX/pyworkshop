nameFile = input("enter name of the file: ")

try: 
    with open(f'{nameFile}', 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError as e:
    print("file xaina")
