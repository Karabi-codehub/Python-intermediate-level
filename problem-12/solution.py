while True:
    # Take input from the user
    user_input = input("Enter command (or type 'exit' to quit): ")
    
    # Check if the user wants to stop
    if user_input.lower() == "exit":
        print("Goodbye!")
        break  # Exit the loop

    # Split the input into command and numbers
    parts = user_input.split()

    # Check if the input is valid (must have 3 parts)
    if len(parts) != 3:
        print("Invalid input! Example: add 5 7")
        continue  # Go back to ask again

    # Extract command and convert numbers
    command = parts[0]
    try:
        num1 = float(parts[1])
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers!")
        continue

    # Perform the operation
    if command == "add":
        result = num1 + num2
    elif command == "subtract":
        result = num1 - num2
    elif command == "multiply":
        result = num1 * num2
    elif command == "divide":
        if num2 == 0:
            result = "Cannot divide by zero!"
        else:
            result = num1 / num2
    elif command == "power":
        result = num1 ** num2
    elif command == "mod":
        result = num1 % num2
    elif command == "max":
        result = max(num1, num2)
    elif command == "min":
        result = min(num1, num2)
    else:
        result = "Unknown command!"

    # Print the result
    print("Result:", result)
