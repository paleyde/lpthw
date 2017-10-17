students = raw_input()
seats = raw_input()

if students > seats:
    print "no seats"	
elif students < seats:
    print "seats are available"
else:
    print "equality holds"