# Step 1: Take the user input from the command line
user_input = input("Enter your command : ")

# Step 2: Split the input into parts
parts=user_input.split()
# Example: "add 5 7" becomes ['add', '5', '7']

# Step 3: Extract command and numbers
command = parts[0]           # 'add' (the operation)
num1 = int(parts[1])         # '5' -> 5 (converted to integer)
num2 = int(parts[2])         # '7' -> 7

# Step 4: Use if/elif to do the correct calculation
if command == "add" or command == "+":
    result = num1 + num2
elif command == "subtract" or command == "-":
    result = num1 - num2
elif command == "multiply" or command == "*":
    result = num1 * num2
elif command == "divide" or command == "/":
    result = num1 / num2
else:
    result = "Unknown command"

print("Result:",result)