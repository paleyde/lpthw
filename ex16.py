from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "copying from %s to %s " % (from_file,to_file)

in_file = open(from_file)
in_text = in_file.read()

print "inputed file is %r bytes long" % len(in_text)
print "does the output file exists: %s" % exists(to_file)
raw_input()

out_file = open(to_file, "w")
out_txt = out_file.write(in_text)
#print "outputed file is %r bytes long" % len(out_text)


print ("all is done")
in_file.close()
out_file.close()
