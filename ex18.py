#-- coding: utf-8 --
#!/usr/bin/python
#Exercise 18 from Learn Python the Hard Way
#Functions

#this is like one of your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this one takes one arguement
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguements
def print_none():
	print "I got nothing"

print_two("Zed", "Shaw")
print_two_again("Jon", "Winegar")
print_one("First")
print_none()
