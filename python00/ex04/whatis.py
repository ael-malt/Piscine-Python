from sys import argv
from sys import exit

try:
	try:
		# Check if we have argv[1], else sys.exit() - not "exit()" since it relies on the `site` module
		if len(argv) < 2:
			exit()

		# Check if we have too many arguments
		if len(argv) > 2:
			raise AssertionError("more than one argument is provided")
		
		# Check if arg[1] is a valid integer
		nb = int(argv[1])
	except ValueError:
		raise AssertionError("argument is not an integer")
	
		# If we do have an integer check if it is even or odd
	if(nb % 2 == 0):
		print("I'm Even.")
	else:
		print ("I'm Odd.")

except AssertionError as error:
	print(AssertionError.__name__ + ":", error)
