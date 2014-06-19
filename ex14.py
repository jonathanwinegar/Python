# -- coding: utf-8 --
#Example 14 from Learn Python the Hard Way book
#This script requires one command line arguement. A username.
from sys import argv

script, user_name = argv

prompt = '> '

print "Hi %s, I'm the %s script" % (user_name, script)
print "I would like to ask you a few questions"
print "Do you like me %s?" % user_name
likes = raw_input()

print "Where do you live %s?" % user_name
location = raw_input()

print "What kind of computer do you have %s?" % user_name
computer = raw_input()

print """
Alright so you said %r about liking me
You live in %r, what a wonderful place.
And you have a %r computer. Nice.
""" % (likes, location, computer)

