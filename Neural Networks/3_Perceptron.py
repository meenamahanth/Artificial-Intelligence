x1 = [-1,-1,1,1]
x2 = [-1,1,-1,1]
gates = { 
          1: [-1,-1,-1,1],
          2: [-1,1,1,1],
          3: [-1,-1,1,-1] }
while True:
    print("Choose the number for the respective Gate \n 1 - AND GATE \n 2 - OR GATE \n 3 - ANDNOT GATE")
    n = int(input())   # 2
    if n not in gates:
        print("Invalid Number Choose the number correctly")
        continue
    gate = gates[n]
    break
print("Enter theta and alpha value with spaces") # 0 1
theta,alpha = map(int,input().split())  # int type
epoch = 0
w1,w2,b = 0,0,0
while True:
    w1n = []
    w2n = []
    bn = []
    yin = []
    y = []
    comp = []
    epoch +=1
    print(f'Epoch {epoch:<5}')
    print(f"{'x1':<5}{'x2':<5}{'t':<5}{'w1':<5}{'w2':<5}{'b':<5}{'yin':<5}{'y':<5}{'Compare y & t':<18}{'w1n':<5}{'w2n':<5}{'bn':<5}")
    for i in range(len(x1)):
        yin.append(w1*x1[i]+w2*x2[i]+b)   # yin = w1*x1 + w2*x2 + b
        if yin[i] > theta:     # Step Function 
            y.append(1)      # yin > theta then y = 1
        elif yin[i] == theta:
            y.append(0)    # yin = theta then y = 0
        elif yin[i] < theta:
            y.append(-1)   # yin < theta then y = -1
        if y[i] == gate[i]:
            comp.append("Equal")
        else:
            comp.append("Not Equal")
        if y[i] != gate[i]:
            w1n.append(w1+alpha*x1[i]*gate[i])
            w2n.append(w2+alpha*x2[i]*gate[i])
            bn.append(b+alpha*gate[i])
            print(f"{x1[i]:<5}{x2[i]:<5}{gate[i]:<5}{w1:<5}{w2:<5}{b:<5}{yin[i]:<5}{y[i]:<5}",end=' ')
            w1,w2,b = w1n[i],w2n[i],bn[i]
            print(f'{comp[i]:<18}{w1n[i]:<5}{w2n[i]:<5}{bn[i]:<5}')
        else:
            w1n.append(w1)
            w2n.append(w2)
            bn.append(b)
            w1,w2,b = w1n[i],w2n[i],bn[i]
            print(f"{x1[i]:<5}{x2[i]:<5}{gate[i]:<5}{w1:<5}{w2:<5}{b:<5}{yin[i]:<5}{y[i]:<5}{comp[i]:<18}{w1n[i]:<5}{w2n[i]:<5}{bn[i]:<5}")
    if "Not Equal" in comp:
        print("This Epoch contains Some Unequalities in comparision so next epoch")
    else:
        print(f"Epoch {epoch} the Comparision got equals")
        break