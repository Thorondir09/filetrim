#imports
import sys
import os

#variables
content = []
start = 0
end = 0
wrout = 0
prout = 0
infile = ''
outfile = ''
err = 0

#main class with i/o functions
class Handler:
	def __init__ (self, f):
		#todo?
		for line in f:
			content.append(line)
	
	def find(self, phrase) :
		#script to find start and end words
		for line in range(len(content)):
			if phrase in content[line] :
				return(line)
				
	def printout(self, start, end):
		for i in range(end - start - 1):
			print content[start + i + 1],
				
	def write(self, start, end, name):
		newfile = open(name, 'w+')
		for i in range(end - start - 1):
			newfile.write(content[start + i + 1])
			
#command argument handling
def help():
	global err
	print 'filetrim, a program that trims out only the parts of a file that you want'
	print 'usage: filetrim [options] [file] [start] [end]'
	print 'options:'
	print '    -p print output instead of writing to file'
	print '    -o [file name] write output to file'
	err = 1

if len(sys.argv) > 4 :
	if sys.argv[1] == '-p':
		prout = 1
		wrout = 0
	elif sys.argv[1] == '-w':
		wrout = 1
		prout = 0
		outfile = sys.argv[2]
	else :
		help()
		
	if wrout == 1 :
		infile = sys.argv[3]
		start = sys.argv[4]
		end = sys.argv[5]
	else :
		infile = sys.argv[2]
		start = sys.argv[3]
		end = sys.argv[4]
		
else :
	help()

# error handling
if err == 1 :
	print 'something went wrong, quitting'
else :

	f = open(infile, 'r')
	trimmer = Handler(f)
	start = trimmer.find(start)
	end = trimmer.find(end)
	if wrout == 1:
		trimmer.write(start, end, outfile)
		print 'done'
	else :
		trimmer.printout(start, end)
