import math
def sigmoidbinary(x):
    return 1/(1+math.exp(-x))
def sigmoidbipolar(x):
    return (2/(1+math.e**(-x))-1)
print("Choose a respective no to select \n 1 - Binary \n 2 - Bipolar \n ")
n=int(input())
print("Enter x1 input values ")
x1 = int(input())
print("Enter x2 input values")
x2 = int(input())
print("Enter t ( target ) output value ")
t = int(input())
print("Enter learning rate (alpha) value ")   # Won't considered lambda as it's value is always 1
l_r = float(input())    
print("Enter weights ( v1 and v2 ) for first hidden layer neuron values")
wh11,wh12 = map(float,input().split())
print("Enter weights ( v3 and v4 ) for second hidden layer neuron values")
wh21,wh22 = map(float,input().split())
print("Enter the weights ( w1 and w2 ) for output layer neuron values")
wo1,wo2 = map(float,input().split())
print("Enter biases starting from first hidden layer neuron, second hidden layer neuron and output layer neuron with spaces")
b1,b2,b3 = map(float,input().split())

# Seleting Sigmoid function ( binary or bipolar ) from n input
if n == 1:
    sigmoid = sigmoidbinary
else:
    sigmoid = sigmoidbipolar

# Forward Pass for Hidden Layers
z1in = wh11 * x1 + wh12 * x2 + b1
z1 = sigmoid(z1in)
z2in = wh21 * x1 + wh22 * x2 + b2
z2 = sigmoid(z2in)
# Forward Pass for output layer
yin = wo1 * z1 + wo2 * z2 + b3
y = sigmoid(yin)
print(f"\nForward Pass\n1 (HN) -> z1in: {z1in:.4f} z1: {z1:.4f}\n2 (HN) -> z2in: {z2in:.4f} z2: {z2:.4f}\n3 (ON) -> yin: {yin:.4f} y: {y:.4f}")

# Backward Pass Error Calculation at output layer
err = (t-y)*y*(1-y) if n==1 else (0.5)*(t-y)*(1+y)*(1-y)
print(f"\nBackward Pass = Error at ON Layer is error: {err:.4f}")
# Backward Pass Error Calculation at hidden layers
err1 = (wo1 * err) * z1 * (1-z1) if n==1 else (0.5) * (wo1 * err) * (1+z1) * (1-z1)
err2 = (wo2 * err) * z2 * (1-z2) if n==1 else (0.5) * (wo2 * err) * (1+z2) * (1-z2)
print(f"Error at 1 (HN) Layer is error1: {err1:.4f}\nError at 2 (HN) Layer is error2: {err2:.4f}")

# Weight and Bias Updates at Output Neuron
w1new = wo1 + (l_r * err * z1)
w2new = wo2 + (l_r * err * z2)
b3new = b3 + (l_r * err)
print(f"\nAt Output Neuron the new weights and bias are")
print(f"w1new: {w1new:.4f} w2new: {w2new:.4f} b3new: {b3new:.4f}")

# Weight and Bias Updates at Hidden Neuron 1
v1new = wh11 + (l_r * err1 * x1)
v2new = wh12 + (l_r * err1 * x2)
b1new = b1 + (l_r * err1)
print(f"\nAt 1 (HN) Layer the new weights and bias are")
print(f"v1new: {v1new:.4f} v2new: {v2new:.4f} b1new: {b1new:.4f}")

# Weight and Bias Updates at Hidden Neuron 2
v3new = wh21 + (l_r * err2 * x1)
v4new = wh22 + (l_r * err2 * x2)
b2new = b2 + (l_r * err2)
print(f"\nAt 2 (HN) Layer the new weights and bias are")
print(f"v3new: {v3new:.4f} v4new: {v4new:.4f} b2new: {b2new:.4f}")