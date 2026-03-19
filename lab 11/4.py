# 4. Implement a system that automatically determines the threshold
# value required for a neuron to correctly simulate AND, OR, and
# NAND gates.
import itertools
gates = {
"AND":[0,0,0,1],
"OR":[0,1,1,1],
"NAND":[1,1,1,0]
}
inputs = list(itertools.product([0,1],[0,1]))
weights = [1,1]
for gate in gates:
    print("\nGate:",gate)
    for t in [0,0.5,1,1.5,2]:
        outputs=[]
        for x in inputs:
            net = x[0]*weights[0] + x[1]*weights[1]
            y = 1 if net >= t else 0
            outputs.append(y)
        if outputs == gates[gate]:
            print("Threshold =",t)
print("Raja Kumar Sah, 23053769")