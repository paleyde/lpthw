from sys import argv

script,user_name = argv
prompt = ':'

print "hi %s , this is %s" % (user_name , script)
print "do u like me %s" % user_name
ans = raw_input(prompt)
print "just tell me the reason, %s" % user_name
res = raw_input(prompt)
print "tell me your age %s" % user_name
age = raw_input(prompt)
print """
your ans is %r
with %r reason.
and your age is %r.
""" % (ans , res , age)


