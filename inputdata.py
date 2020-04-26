# fullname = input("Enter your name:")
# age = input("Enter your age:")
# print(fullname)
# print(age+5)

user = input("Enter username:")
pwd = input("Enter password:")
user = user

if user.lower() == "admin" and pwd == "1234":
    print("Yah! login success")
else:
    print("Opp! login faill!!")
