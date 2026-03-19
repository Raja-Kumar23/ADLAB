# 10. Develop a system where multiple McCulloch–Pitts neurons
# collaborate to perform pattern recognition for binary images.
import numpy as np
pattern = np.array([
[1,1,1],
[0,1,0],
[1,1,1]
])
test = np.array([
[1,1,1],
[0,1,0],
[1,1,1]
])
similarity = np.sum(pattern == test)
if similarity > 7:
    print("Pattern Recognized")
else:
    print("Not Recognized")
print("Raja Kumar Sah, 23053769")