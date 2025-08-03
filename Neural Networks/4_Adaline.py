x1 = [1,-1,1,-1]
x2 = [1,1,-1,-1]
gates = { 
          1: [1,-1,-1,-1],
          2: [1,1,1,-1],
          3: [-1,-1,1,-1] }
while True: # hebb lo enduku oka while loop aa ante akkadha compare cheyyali kani ikkadha comparision vundhadhu and no of epochs vuntai
    print("Choose the number for the respective Gate \n 1 - AND GATE \n 2 - OR GATE \n 3 - ANDNOT GATE")
    n = int(input())  # 2
    if n not in gates:
        print("Invalid Number Choose the number correctly")
        continue
    gate = gates[n]
    break
print("Enter No of Epochs you want ")
e = int(input())  # 3
epoch = 0
w1,w2,b = 0.1,0.1,0.1
print("Enter the learning-rate (alpha) value ")
l_r = float(input()) # 0.1 - float type
for i in range(e):
    w1n = []
    w2n = []
    bn = []
    yin = []
    err = []
    se = []
    epoch +=1
    print(f'Epoch {epoch}')
    print(f"{'x1':<5}{'x2':<5}{'t':<5}{'w1':<8}{'w2':<8}{'b':<8}{'yin':<8}{'Error':<8}{'w1n':<8}{'w2n':<8}{'bn':<8}{'SE':<8}")
    for i in range(len(x1)):
        yin.append(w1*x1[i]+w2*x2[i]+b)
        err.append(gate[i]-yin[i])
        w1n.append(w1+l_r*err[i]*x1[i])
        w2n.append(w2+l_r*err[i]*x2[i])
        bn.append(b+l_r*err[i])
        se.append(err[i]*err[i])
        print(f"{x1[i]:<5}{x2[i]:<5}{gate[i]:<5}{w1:<8.3f}{w2:<8.3f}{b:<8.3f}{yin[i]:<8.3f}{err[i]:<8.3f}{w1n[i]:<8.3f}{w2n[i]:<8.3f}{bn[i]:<8.3f}{se[i]:<8.3f}")
        w1,w2,b = w1n[i],w2n[i],bn[i]
    print(f"Average of Mean Squared Error: {sum(se)/len(se):.3f} \n")