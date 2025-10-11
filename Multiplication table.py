def multiplication_table():
    print("Multiplication Table (9x9)")
    print("=" * 50)
    
    # Method 1: Simple nested loops
    print("\nMethod 1 - Basic Table:")
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j:2d}", end="  ")
        print()
    
    # Method 2: Compact format
    print("\n" + "=" * 50)
    print("Method 2 - Compact Format:")
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i*j:2d}", end=" ")
        print()
    
    # Method 3: With row headers
    print("\n" + "=" * 50)
    print("Method 3 - With Headers:")
    print("   ", end="")
    for i in range(1, 10):
        print(f"{i:3d}", end="")
    print()
    print("  " + "-" * 30)
    
    for i in range(1, 10):
        print(f"{i} |", end="")
        for j in range(1, 10):
            print(f"{i*j:3d}", end="")
        print()

def multiplication_table_advanced():
    print("\n" + "=" * 50)
    print("Advanced Multiplication Table")
    print("=" * 50)
    
    # Create a grid with borders
    print("   +", end="")
    for i in range(1, 10):
        print("---", end="")
    print("+")
    
    for i in range(1, 10):
        print(f"{i} |", end="")
        for j in range(1, 10):
            print(f"{i*j:3d}", end="")
        print(" |")
    
    print("   +", end="")
    for i in range(1, 10):
        print("---", end="")
    print("+")

def multiplication_table_triangle():
    print("\n" + "=" * 50)
    print("Triangular Multiplication Table")
    print("=" * 50)
    
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j} x {i} = {i*j:2d}", end="   ")
        print()

def interactive_multiplication_table():
    print("\n" + "=" * 50)
    print("Interactive Multiplication Table")
    print("=" * 50)
    
    while True:
        try:
            number = int(input("Enter a number (1-9) to see its table (0 to exit): "))
            if number == 0:
                print("Goodbye!")
                break
            elif 1 <= number <= 9:
                print(f"\nMultiplication Table for {number}:")
                print("-" * 20)
                for i in range(1, 10):
                    print(f"{number} x {i} = {number * i}")
                print()
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")

# Run all versions
if __name__ == "__main__":
    multiplication_table()
    multiplication_table_advanced()
    multiplication_table_triangle()
    
    # Uncomment the line below for interactive version
    # interactive_multiplication_table()