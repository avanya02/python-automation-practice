#Read a file and write another file

with open('users.txt', 'r') as file:
    data = file.readlines() 
    print(data)

with open('output.txt', 'w') as file:
    for name in data:
        file.write(name.strip().upper() + '\n')
