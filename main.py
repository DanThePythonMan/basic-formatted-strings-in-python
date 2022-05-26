conf1 = "0"
while conf1=="0":
    mothername=input("What is your mother's name? ")
    #formatted string V
    conf=input(f"Are you sure your mother's name is {mothername} ? ")
    if conf == "yes":
        print(mothername)
        conf="1"
    else:
        print("Either you were not understood or you cancelled")

print (mothername)
