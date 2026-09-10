name = input("Input your name:  ")
age = int(input("Input your age:  "))

if age >= 60 and age <= 150:
    print("Senior")
elif age >= 49 and age <= 59:
    print("Advance adult")
elif age >= 30 and age <= 48:
    print("Adult")
elif age >= 20 and age <= 29:
    print("Early Adult")
elif age >= 13 and age <= 19:
    print("Teeneger")
elif age >= 6 and age <= 12:
    print("Advance adult")
elif age >= 1 and age <= 5:
    print("Infant")
else:
    print("Invalid")
