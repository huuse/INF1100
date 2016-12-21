#interest_rate.py


A = 1000
#input("set inital amount of money ")

p = 5
#input("set interest rate ")

n = 3
#input("set years ")

s = A*(1+(p)/(100.0))**2

#print(s)


print("After %s years, %s euros has grown to %s euros with an interest rate at %s %%" %(n, A, s, p))
