Age = 0

while Age < 30:
    Age = Age + 1
    print(Age)

#El While se ejecuta hasta que se ingresa un número impar
while True:
    value_input = int(input("Input a pair number: "))
    if value_input % 2 != 0:
        print ("This is not a pair number")
        break
    print ("Good, is a pair number!")