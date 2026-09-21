print("\n")
print("name - Om Kartike")
print("gu_id - 26SSSE3020031")
print("student-email - om.26ssse3020031@galgotiasuniversity.ac.in")
print("\n")


units = float(input("Enter the units consumed: "))
total_bill = 0.0

if units <= 100:
    total_bill = units * 1.5
elif units <= 200:
    total_bill = (100 * 1.5) + \
                 ((units - 100) * 2.0)
else:
    total_bill = (100 * 1.5) + \
                 (100 * 2.0) + \
                 ((units - 200) * 3.0)

print(f"Amount Due: Rs.{total_bill:.2f}")

