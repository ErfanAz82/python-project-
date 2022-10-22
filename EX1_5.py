age = float(input("Please enter your age: "))
if age <= 1:
    print("You are an infant.")
elif age < 13:
    print("You are an child.")
elif age < 20:
    print("You are an teenager.")
elif age >= 20:
    print("You are an adult.")