#!/usr/bin/python
# -- coding: utf-8 --
#Example 16 from Learn Python the Hard Way
#

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl-C."
print "If you do want that hit RETRUN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')



target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I am going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally we close it"

target.close()
