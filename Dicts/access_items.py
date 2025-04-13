thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]

print(x)

y = thisdict.get("brand")

print(y)

z = thisdict.keys()
zz = thisdict.values()

print(z, zz)

thisdict["color"] = "White"

print(thisdict["color"])


# The items() method will return each item in a dictionary, as tuples in a list.

a = thisdict.items()

print(a)

if "model" in thisdict: 
    print("Yes, 'model' is one of the keys in the thisdict dictionary")