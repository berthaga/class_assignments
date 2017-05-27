#Example One
name='Bertha'
female='Bertha'
if name==female:
	print "Welcome"
else:
	print "No"


#Example Two
name='Bertha'
female='Alex'
if name==female:
	print "Welcome"
else:
	print "No"


#Example Three
name=raw_input("what is your favourite car?:")
if name=="range rover":
	print 'Tata'
else:
	print name

#Example Four
name=raw_input("what is your favourite car?:")
if name=="range rover":
	print 'Tata'
else:
	print name	
	new_Nmae=raw_input("Manufacturer?")
	print "It was manufactured by " +  new_Nmae


#Example Four
name=raw_input("what is your favourite car?:")
if name=="range rover":
	print 'It wa manufacftured by Tata'
elif name=="toyota":
	print 'It wa manufacftured by Toyota'
else:
	print "I don't know"