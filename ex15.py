from sys import argv

script, filename = argv

print "this is %s script." % script
file = raw_input(":")
text = open(file)
print text.read()