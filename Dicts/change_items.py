thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

print(thisdict)

thisdict.update({"year": 2025})

print(thisdict)

thisdict["color"] = "red"

print(thisdict)

thisdict.update({"color": "blue"})

print(thisdict)