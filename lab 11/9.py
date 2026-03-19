# 9. Implement a multi-neuron logical circuit using McCulloch–Pitts
# neurons to simulate a simple digital circuit (e.g., half adder).
def neuron(x,w,t):
    net = x[0]*w[0] + x[1]*w[1]
    return 1 if net>=t else 0
inputs = [[0,0],[0,1],[1,0],[1,1]]
print("Half Adder")
for x in inputs:
    sum_bit = neuron(x,[1,-1],1) or neuron(x,[-1,1],1)
    carry = neuron(x,[1,1],2) 
    print(x,"Sum:",sum_bit,"Carry:",carry)
print("Raja Kumar Sah, 23053769")