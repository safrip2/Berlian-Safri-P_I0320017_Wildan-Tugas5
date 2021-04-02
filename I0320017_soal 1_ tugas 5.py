def welcome():
    print("\t\tWelcome to Daystar Hotel and Resto")
def greet_user(name):
    print(f"Hello {gender} {name}!")
print("\t\t\t\t-----🔆------")
welcome()
print("before book our services, you must sign up here")
name = input("what is your Name? ")
gender = input("""you are?\n1.male\n2.female \n3.prefer not to say """)
if gender.upper() == "MALE" or gender == "1":
    gender = "Mr."
    greet_user(name)
elif gender.upper() == "FEMALE" or gender == "2":
    gender = "Mrs."
    greet_user(name)
elif gender.upper() == "PREFER NOT TO SAY" or gender == "3":
    print(f"Hello {name}")
else:
    pass



