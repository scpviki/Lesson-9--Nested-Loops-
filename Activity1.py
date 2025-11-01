medical_cause=input("Do you have a medical cause Y or N=")
attendance=int(input("Enter your attendance"))
if medical_cause=="y":
    print("You are allowed")
else:
    if attendance>=75:
        print("You are allowed")
    else:
        print("you are not allowed")