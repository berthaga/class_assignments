for letter in 'python':
	if letter=='p':
		continue
	print letter



fruits=['mango','pawpaw','banana','apple','grapes','watermellon','pineapple']
for item in fruits:
	if item =='banana':
	    print item, ' You have chosen the best fruit'
	else:
		print item, 'Okey. Good choice'



location=['accra','labone','tema','lapaz','ashaiman','sunyani']
for place in range(len(location)):
	print place
	print location[place]


month={'jan':'january','feb':'february','mar':'march','apr':'april','may':'may','jun':'june','jul':'july','aug':'agust','sep':'september','oct':'october','nov':'november','dec':'december'}
for day in range(len(month)):
	print day
	print month
	print month.values()
	print month.keys()


for letter in 'python':
	if letter=='o':
		break
	print letter

for letter in 'python':
	if letter=='o':
		pass
		print 'passing it'
	print letter

for x in 'abcdef':
	print x
else:
	print 'the end'