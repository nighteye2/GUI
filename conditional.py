attendance = float(input("Enter your attendance percentage: "))
if attendance>98:
    print("you are Anuj ")
elif attendance>=75 and attendance<98:
    print("you are eligible")
elif attendance<75:
    print("you are not eligible")
elif attendance<30:
    print("you are kedar")
else:
    print("enter a valid age") 