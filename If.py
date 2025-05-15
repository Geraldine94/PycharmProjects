balance = 500
if balance > 0:
    print ("You can pay")

balance2 = 500
if balance2 > 501:
    print ("You can pay")

balance3 = 0
if balance3 > 0:
    print ("You can pay")
else:
    print ("You can´t founding")

likes = 200
if likes == 200:
    print ("Great! you're popular")
else:
    print("C´mon, keep going!")

nationality = 'Argentina'
if nationality == 'Argentina':
    print ("You're argentinian, Messi is the best!")

nationality = 'Mexico'
if not nationality == 'Argentina':
    print ("They stole the World cup!")

computer_on: bool
computer_on=True

#en los valores booleanos se revisa automáticamente si la condición es verdadera o falsa, no es necesario especificarla
if computer_on:
    print ("You can program")
else:
    print ("Turn on the computer")

user_authenticated = True
user_admin = True

if user_authenticated:
    if user_admin:
        print ("Total access")
    else:
        print ("Partial access")
else:
    print ("You must log in")

#Else if en Python es elif
occupation = "Unemployed"

if occupation == "Student":
    print("You have 50% of discount")
elif occupation == "Unemployed":
    print("You have 75% of discount")
else:
    print("You haven´t discount")