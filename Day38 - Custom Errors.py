a=int(input("enter any value between 5 and 9:"))
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")


b = input("Enter any value between 5 and 9: ")

# Check for the "quit" command
if b.lower() == "quit":
    exit()

try:
    # Convert input to an integer
    b = int(b)
    
    # Validate the range
    if b < 5 or b > 9:
        raise ValueError("Value should be between 5 and 9.")
    else:
        print(f"Your input is valid: {b}")
except ValueError as e:
    print(f"Invalid input: {e}")


