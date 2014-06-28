# -- coding: utf-8 --
#!/usr/bin/python/
#Exercise 17 from Learn Python the Hard Way

from sys import argv

from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s.\n" % (from_file, to_file)

in_file = open(from_file)

indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

print "Ready, hit Ctrl-C to exit, Return to continue."

raw_input()

out_file = open(to_file, 'w')

out_file.write(indata)

print "Alright all done"

out_file.close()
in_file.close()
