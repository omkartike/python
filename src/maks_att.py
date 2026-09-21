#program for marks and attendence (wether student is eligible or not)

print("\n")
print("name - Om Kartike")
print("gu_id - 26SSSE3020031")
print("student-email - om.26ssse3020031@galgotiasuniversity.ac.in")
print("\n")

marks = int(input("enter the marks obtained : ")) # 0-100
attendance_percentage = float(input("Enter attendance percentage: ")) # 0-100

if marks >= 50 and attendance_percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")