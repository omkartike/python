print("\n")
print("name - Om Kartike")
print("gu_id - 26SSSE3020031")
print("student-email - om.26ssse3020031@galgotiasuniversity.ac.in")
print("\n")


age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
