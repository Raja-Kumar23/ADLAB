# 7. Convert a categorical column into numeric using label encoding manually.
import pandas as pd 
data=pd.DataFrame({
    "color":["red","blue","green"]
})
mapping={"red":0,"blue":1,"green":2}
data["color_num"]=data["color"].map(mapping)
print(data)
print("Name: Raja Kumar")
print("Roll: 23053769")