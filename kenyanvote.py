age = int(input("Enter your age: "))
is_kenyan_citizen = input("Are you a Kenyan citizen? (yes/no): ").lower()
if age >= 18 and is_kenyan_citizen == "yes":
    print("You are eligible to vote in Kenya.")
else:
    print("You are not eligible to vote in Kenya.")
