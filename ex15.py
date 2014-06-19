# -- coding: utf-8 --
#Example 15 from Learn Python the Hard Way
#This script requires 1 command line arguement. A file name. Specifically ex15_sample.txt.
from sys import argv
script, filename = argv

text = open(filename)

print "Here is your file %r: " % filename
print text.read()

print "Type the filename again:"
file_again = raw_input("> ")

text_again = open(file_again)

print text_again.read()


