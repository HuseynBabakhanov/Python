# # name = input("Enter your full name: ")
# phone_number = input("Enter your phone#: ")
# # result = len(name)  #This function returns an integer
# # result = name.find("o")
# # result = name.rfind("q")
# # name = name.capitalize()
# # name = name.upper()
# # name = name.lower()
# # result = name.isdigit()
# # result = name.isalpha()
# # result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")




# print(phone_number)

# print(help(str))

# Practice


username = input("Enter a username: ")

username.find(" ")

username.isalpha()

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")


