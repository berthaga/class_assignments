# for loops with continue function 

x=['mon','tues','wed','thur','fri','sat','sun']
for days in x:
	if days=='wed':
		continue
	print days

# for loops with pass function 	
x=['mon','tues','wed','thur','fri','sat','sun']
for days in x:
	if days=='wed':
		pass
		print'passing wednesday' 
	print days

# for loops with break function 
x=['mon','tues','wed','thur','fri','sat','sun']
for days in x:
	if days=='wed':
		break 
	print days

# while loops with continue function 

x=100
while x<=110:
	x=x+1
	if x==105:
		print 'Exact number'
		continue
	print x
	print 'best choice'

# while loops with break function 

x=100
while x<=110:
	x=x+1
	if x==105:
		print 'Exact number'
		break
	print x
	print 'best choice'

# while loops with pass function
	
x=100
while x<=110:
	x=x+1
	if x==105:
		pass
		print 'passing Exact number'
	print x
	print 'best choice'
	