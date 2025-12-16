#Write a Python program to sort a dictionary by value.
my_dict = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 5}
sorted_keys = sorted(my_dict, key=my_dict.get)    
sorted_dict = {}
for k in sorted_keys:
    sorted_dict[k] = my_dict[k]
    print("Sorted dictionary by value:", sorted_dict)
    print("Name:Raja Kumar Sah")
    print("Roll:23053769")
































