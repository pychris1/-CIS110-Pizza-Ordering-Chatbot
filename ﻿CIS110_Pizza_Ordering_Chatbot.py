print ("Hello I am Jarvis, your virtual pizza ordering assistant! With Whom do I have the pleasure of assisting today?")
userName = input("\nEnter your name: ")
if userName.lower() == "james":
    print(f"\nWe meet again, Master {userName}. Lets get started with some pizza!")
else:
    print(f"\nHello, Master {userName}. Nice to meet you!")


#What Pizza we want

size = input(f"\nWhat size pizza would you like Master {userName}? I have small, medium and large: ")
flavor = input(f"\nWhat flavor would you like Master {userName}? I heard the Buffalo or Parmesean flavor is to die for: ")
crustType = input(f"\nWhat type of crust would you like Master {userName}? Maybe stuffed or even thin if you are looking to cut some calories: ")
qauntity = input(f"\nGreat! Now how many should I order Master {userName} Please enter a numeric value: ")
qauntity = int(qauntity)
method = input(f"\nLastly, Now is this carryout or delivery Master {userName}: ")

if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0

salesTax = 1.1

if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
total = (pizzaCost * qauntity) * salesTax + deliveryFee

print("-" * 10)
print(f"Thank you, {userName}, for your order.")
print(f"Your {qauntity} {size} {flavor} pizzas(s) with {crustType} crust costs ${total:,.2f}.")
print("-" * 10)

if total >= 50:
    print("\nCongratulations! You've been awarded a $10 Off coupon for your next order.")
else:
    print("\nOrder over $50 will reecieve a free $10 Off coupon!")
    
print("-" * 10)


