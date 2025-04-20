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


# items() returns a list containing a tuple for each key/value pair
# keys() returns a list containing the dictionaries keys
# pop() removes the element with a specified key
# popitem() removes the last inserted key-value pair
# setdefault() returns the value of a specified key
# update() updates the dict with the specified key-value pairs
# values() returns a list of all values in the dict. 