gates_binary = { 1: [0,0,0,1],
                 2: [0,1,1,1],
                 3: [0,0,1,0] }
gates_bipolar = { 1: [-1, -1, -1, 1], 
                  2: [-1, 1, 1, 1],     
                  3: [-1, -1, 1, -1] }
while True:
    print("Choose the respective no to Select \n 1-Binary \n 2- Bipolar")
    choice = int(input())  # 2
    if choice == 1:
        x1 = [0,0,1,1]
        x2 = [0,1,0,1]
        gates = gates_binary
    elif choice ==2:
        x1 = [-1,-1,1,1]
        x2 = [-1,1,-1,1]
        gates = gates_bipolar
    print("Choose the number for the respective Gate \n 1 - AND GATE \n 2 - OR GATE \n 3 - ANDNOT GATE")
    n = int(input())  # 1
    if n not in gates:
        print("Invalid Number Choose the number correctly")
        continue
    gate = gates[n]
    break
w1, w2, b = 0,0,0
w1n =[]
w2n = []
bn = []
print(f"{'x1':<5}{'x2':<5}{'t':<5}{'w1':<5}{'w2':<5}{'b':<5}{'w1n':<5}{'w2n':<5}{'bn':<5}")
for i in range(len(x1)):
    w1n.append(w1+x1[i]*gate[i])  # w1new = w1old + x1*t
    w2n.append(w2+x2[i]*gate[i])  # w2new = w1old + x2*t
    bn.append(b+gate[i])     # bnew = bold + t
    print(f"{x1[i]:<5}{x2[i]:<5}{gate[i]:<5}{w1:<5}{w2:<5}{b:<5}{w1n[i]:<5}{w2n[i]:<5}{bn[i]:<5}")
    w1, w2, b = w1n[i], w2n[i], bn[i]
print(f'The Final Weights are w1 = {w1n[-1]}, w2 = {w2n[-1]}, b = {bn[-1]}')