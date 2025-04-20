pc_dict = dict(cpu="R9 7950X3D", gpu="RTX 3090ti", ram="64GB", g_drive="2TB SSD", c_drive="4TB HDD")

# clear() removes all elements from a dictionary
pc_dict_clear = dict(pc_dict)
pc_dict_clear.clear()
print("pc_dict_clear: ", pc_dict_clear)

# copy() returns a copy of a dictionary
pc_dict_copy = pc_dict.copy()
print("pc_dict_copy: ", pc_dict_copy)


# fromkeys() returns a dictionary with the specified keys and values

pc_dict_fromkeys = pc_dict.fromkeys("12345")
print("pc_dict_fromkeys: ", pc_dict_fromkeys)


# get() returns the value of a specified key
pc_dict_get = pc_dict.get("cpu")
print("pc_dict_get: ", pc_dict_get)


# items() returns a list containing a tuple for each key/value pair

pc_dict_items = pc_dict.items()
print("pc_dict_items: ", pc_dict_items)

# keys() returns a list containing the dictionaries keys
pc_dict_keys = pc_dict.keys()
print(pc_dict_keys)

# values() returns a list of all values in the dict. 
pc_dict_values = pc_dict.values()
print(pc_dict_values)

# pop() removes the element with a specified key

pc_dict_pop = pc_dict.copy()
pc_dict_pop.pop("cpu")

print("pc_dict_pop: ", pc_dict_pop)

# popitem() removes the last inserted key-value pair

pc_dict_popitem = pc_dict.copy()
pc_dict_popitem.popitem()
print(pc_dict_popitem)

# setdefault() returns the value of a specified key

pc_dict_setdefault = pc_dict.setdefault("gpu")
print(pc_dict_setdefault)
print(pc_dict["gpu"])


# update() updates the dict with the specified key-value pairs
pc_dict_update = pc_dict.copy()
pc_dict_update.update(motherboard="Tomohawk X870")

print(pc_dict_update)