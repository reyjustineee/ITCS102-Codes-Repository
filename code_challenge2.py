cash = 6836

print("Cash to deposit:", cash)

a = cash//1000
cash = cash - a*1000
b = cash//500
cash = cash - b*500
c = cash//200
cash = cash - c*200
d = cash//100
cash = cash - d*100
e = cash//50
cash = cash - e*50
f = cash//20
cash = cash - f*20
g = cash//10
cash = cash - g*10
h = cash//5
cash = cash - h*5
i = cash//1
cash = cash - i*1



print("\nI have ", a, "of 1000")
print("I have ", b, "of 500")
print("I have ", c, "of 200")
print("I have ", d, "of 100")
print("I have ", e, "of 50")
print("I have ", f, "of 20")
print("I have ", g, "of 10")
print("I have ", h, "of 5")
print("I have ", i, "of 1")