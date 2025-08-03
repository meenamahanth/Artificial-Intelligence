x1 = [0,0,1,1]
x2 = [0,1,0,1]
gates = { 1: [0,0,0,1],
          2: [0,1,1,1],
          3: [0,0,1,0] }
while True:
    print("Choose the number for the respective Gate \n 1 - AND GATE \n 2 - OR GATE \n 3 - ANDNOT GATE")
    n = int(input())  # 2 - for OR Gate 
    if n not in gates:
        print("Invalid Number Choose the number correctly")
        continue
    gate = gates[n]
    break
while True:
    print("Assume some values & Enter weight1, weight2, and theta with spaces") # Final Values to get answer is 
    w1,w2,theta = map(int,input().split())                                      # 1 1 1
    yin = []
    y = []
    comp = []
    print(f"{'x1':<5}{'x2':<5}{'yin':<7}{'y':<7}{'Compare y & t'}")
    for i in range(len(x1)):
        yin.append((x1[i]*w1)+(x2[i]*w2))  # yin = x1*w1 + x2*w2
        if yin[i] >= theta:   # Step Function 
            y.append(1)     # yin >= theta then y = 1
        else:
            y.append(0)    # yin < theta then y = 0
        if y[i] == gate[i]:
            comp.append("Equal")
        else:
            comp.append("Not Equal")
        print(f"{x1[i]:<5}{x2[i]:<5}{yin[i]:<7}{y[i]:<7}{comp[i]}")
    if "Not Equal" in comp:
        print("With these weights the comparision contains some inequality.So, Try again with new weights")
    else:
        print("All input patterns comparision gets all equal")
        break