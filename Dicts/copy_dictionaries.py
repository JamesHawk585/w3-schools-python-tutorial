car_dict = dict(brand="Ford", model="Mustang", year=1964)

print("car dict: ", car_dict)


# Make a copy of a dictionary with the copy() method:
mustang_dict = car_dict.copy()
print("mustang dict: ", mustang_dict)

# Make a copy of a dictionary with the dict() function:


chevy_dict = dict(mustang_dict)
chevy_dict["brand"] = "Chevrolet"
chevy_dict["model"] = "Corvette"
chevy_dict["year"] = 1959


print("Chevy dict: ", chevy_dict)