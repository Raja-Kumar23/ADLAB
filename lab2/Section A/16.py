#Check subset and superset.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = True
for x in set1:
    if x not in set2:
        is_subset = False
        break
is_superset = False
for x in set1:
    if x  in set2:
        is_superset = True
        break
print("subset", is_subset)
print("superset", is_superset)
print("Name: Raja Kumar")
print("Roll: 23053769")




