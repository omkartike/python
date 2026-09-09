#area_calculator program

import math

print("------------------------------\n   Area calculator program\n------------------------------")

print("1-Square\n2-Circle\n3-Triangle\n4-Rectangle\n5-Parallelogram")

choice = int(input("Enter your choice : "))

if choice == 1:
    side = int(input("Enter the side : "))
    print(f"The area of the square is {side * side}" )

elif choice == 2:
    radius = int(input("Enter the radius : "))
    print(f"The area of the circle is {math.pi * radius * radius}")

elif choice == 3:
    height = int(input("Enter the height : "))
    base = int(input("Enter the base : "))
    print(f"The area of the triangle is {0.5 * height * base}")

elif choice == 4:
    length = int(input("Enter the length : "))
    width = int(input("Enter the width : "))
    print(f"The area of the rectangle is {length * width}")

elif choice == 5:
    height = int(input("Enter the height : "))
    base = int(input("Enter the base : "))
    print(f"The area of the parallelogram is {height * base}")

else:
    print("Invalid choice")