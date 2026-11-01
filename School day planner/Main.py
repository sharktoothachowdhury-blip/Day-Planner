print("Welcome to your school day planner!")
print("answer these three questions, and i will plan yoour day\n")

day=input("what day is it? (monday to sunday)").strip().capitalize()
weather=input("How is the weather?(sunny,rainy or cloudy)").strip().lower()
homework=input("Have you dont your homework?(yes or no)").strip().lower()
print("\n")
print("your plan for the day will look like this\n")

if day in("Saterday","Sunday"):
    print("Daytype : Weekend : Enjoy your free time")
elif day==("Monday"):
    print("Daytype : First day of the week : Pack your Weekly Planner")
elif day==("Tuesday","Wednesday","Thursday"):
    print("Daytype : Middle of the week : Keep going solider")
elif day==("Friday"):
    print("Daytype : Last Weekday : Weekend Time!!!")
else:
    print("Day of the Week not Found, Check spelling")

