def find_gcd(a, b):
    # Using the Euclidean algorithm to find GCD
    while b:
        a, b = b, a % b
    return a

# Input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function and print the result
gcd = find_gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", gcd)
