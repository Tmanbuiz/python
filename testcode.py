def describe_animal(**pets):
    description = "This animal is "
    for key, value in pets.items():
        description += f"{value} {key} and "
    description = description[:-5]  # Remove the extra "and" at the end
    print(description)

# You can call the function with various keyword arguments:
dog_info = describe_animal(color="brown", size="medium", sound='barks', types= 'Amerian', breed=True)
cat_info = describe_animal(color="gray", size="small", sound="meows", tail="long")

def create_profile(**kwargs):
    profile = {}  # Create an empty dictionary to store the profile
    for key, value in kwargs.items():
        profile[key] = value  # Add each keyword and its value to the profile dictionary
    return profile


# You can call the function with different keyword arguments:
person1 = create_profile(name="Alice", age=30, city="New York")
person2 = create_profile(name="Bob", profession="Engineer", country="Canada")

print(person1)
print(person2)


