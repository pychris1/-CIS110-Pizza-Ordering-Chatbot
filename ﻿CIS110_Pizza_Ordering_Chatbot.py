print ("Hello I am Jarvis, your virtual pizza ordering assistant! With Whom do I have the pleasure of assisting today?")
userName = input("\nEnter your name: ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name: ")
if userName.lower() == "james":
    print(f"\nWe meet again, Master {userName}. Lets get started with some pizza!")
else:
    print(f"\nHello, Master {userName}. Nice to meet you!")

keepGoing = "y"
while keepGoing.lower() == "y":
    size = input(f"\nWhat size pizza would you like Master {userName}? I have small, medium and large: ")
    while size.lower() not in ["small", "medium", "large"]:
        size = input("Invalid value! Please enter small, medium or large: ")
    
    flavor = input(f"\nWhat flavor would you like Master {userName}? I heard the Buffalo or Parmesean flavor is to die for: ")
    while len(flavor) == 0:
        flavor = input("Flavor cannot be blank! Please enter a flavor: ")
    
    crustType = input(f"\nWhat type of crust would you like Master {userName}? Maybe stuffed or even thin if you are looking to cut some calories: ")
    while len(crustType) == 0:
        crustType = input("Crsut type cannot be blank! Please ennter crust type: ")
    
    qauntity = input(f"\nGreat! Now how many should I order Master {userName} Please enter a numeric value: ")
    while not qauntity.isdigit():
        qauntity = input("\nValue not recognized. Please ennter a numeric value: ")
    qauntity = int(qauntity)
    method = input(f"\nLastly, Now is this carryout or delivery Master {userName}: ")
    while method not in ["carry out", "delivery"]:
        method = input("Invalid value! Please enter carry out or delivery: ") 

    salesTax = 1.1
    if size.lower() == "small":
        pizzaCost = 8.99
    elif size.lower() == "medium":
        pizzaCost = 14.99
    elif size.lower() == "large":
        pizzaCost = 17.99
    
    if method.lower() == "delivery":
        deliveryFee = 5
    else:
        deliveryFee = 0
    
    total = (pizzaCost * qauntity) * salesTax + deliveryFee

    print("-" * 10)
    print(f"Thank you, {userName}, for your order.")
    print(f"Your {qauntity} {size} {flavor} pizzas(s) with {crustType} crust costs ${total:,.2f}.")      
    if total >= 50:
        print("\nCongratulations! You've been awarded a $10 Off coupon for your next order.")
    else:
        print("\nOrder over $50 will reecieve a free $10 Off coupon!")
    print("-" * 10)

    print("Order has been received. ETA 3 mins!")
    for min in range(3, 0, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end = "\r")
            import time
            time.sleep(1)
    print("Order is ready!")

    keepGoing = input("Do you want to  place another order? Enter y or n: ")
    while keepGoing.lower() not in ["y", "n"]:
            keepGoing = input("Invalid Value: Enter y or n:")
            

