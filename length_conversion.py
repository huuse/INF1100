#length_conversion.py


l = input("set length in meter  ")


inch1 = l*100/2.54
inch = round(inch1 , 1)

foot1 = inch1/12
foot = round(foot1, 1)

yard1 = foot1/3
yard = round(yard1, 1)

Bmile1 = yard1/1760
Bmile = round(Bmile1 , 1)




print("%sm is %sinches" %(l, inch))

print("%sinches is %sfoot" %(inch, foot))

print("%sfoot is %syard" %(foot, yard))



if Bmile == 0:

	Bmile = round(Bmile1, 2)

if Bmile == 0:

	Bmile = round(Bmile1 , 3)


print("%syard is %sBmile" %(yard, Bmile))
#print inch
