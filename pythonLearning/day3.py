# # booleans
# print()

# temperature = 35
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:("It's cold")
# print("Done")

# age=12
# message = "Eligible" if age >=18 else "Not Eligible"
# print(message)

high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")