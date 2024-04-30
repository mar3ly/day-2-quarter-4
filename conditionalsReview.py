# Ask the user to input the current weather. This can be simplified to three categories for ease: "sunny", "rainy", or "cold".
weather = input("What is the current weather (sunny rainy, cold): ")


# Implement the decision structure to advise on what to wear:
# If the weather is "sunny", recommend "wear sunglasses and a hat".
elif weather = "sunny": 
    print("wear sunglasses and a hat")
# If the weather is "rainy", recommend "carry an umbrella and wear waterproof boots".
elif weather = "rainy":
    print("carry an umbrella and wear waterproof boots")
# If the weather is "cold", recommend "wear a warm coat and gloves".
elif weather = "cold":
    print("wear a warm coat and gloves")
# If the input doesn't match any category, inform the user with a message saying the input was not recognized.
else:
    print("input not recognized, please enter sunny, rainey, cold")
#Next 
# Ask the user to input their age and location. Assume location to be either "urban" or "rural".
age = int(input("what is your age"))
location = input("what id your location? (urban, Rural?)")
# Implement the eligibility checks using comparison and logical operators:
# <, >, >=, <=, ==, !=, and, or, not


# Implement the eligibility checks using comparison and logical operators:

# Participants must be at least 18 years old.
if age >= 18 and location == "urban":
    print("you are eligable to participate")
else:
    print("you are not eligable to participate.")
# Participants must live in an "urban" area.
# Display a message indicating whether the user is eligible or not based on these conditions.
    
if age >= 18 and citizenship == "yes":
    print("you are eligable to vote")
else:
    print("you are not eligable to vote")