#string
hi= "Hello Bertha"
print hi [6:]

#numbers
score1=22
score2=33
score3=33.6
score4=2j+2
total=score1+score2+score3+score4
print total

#list
Drinks=["coke","fanta","malt"]
print 2*Drinks

#Tuples
water=("voltic","standard")
print water[0]


#Dictionary
data={"name":"Bertha","class":"python","level":"beginner"}
print data
print data["name"]

# conditional statement
m=raw_input("what day is today?: ")
if m=="wednesday":
	print m,":There is class today "
elif m=="friday":
	print m,":There is class today "
elif m=="saturday":
	print m,":There is class today "
else:
	print m,":There is no class today"