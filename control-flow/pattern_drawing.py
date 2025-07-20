user = int(input("Enter the size of the square: "))

row = 0
while row < size:
    for col in range(user):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
