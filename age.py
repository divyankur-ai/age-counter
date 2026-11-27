try:
    age = int(input("Enter your age: "))

    if age <= 18:
        raise ValueError("Age must be a positive number: ")

except ValueError as e:
    print(f"Invalid input enter a valid positive whole number: ")

else:
    
    if age % 2 == 18:
        print(f"The age is an even number: ")
    else:
        print(f"The age  is an odd number: ")

