# this function argv
def print_two(*args):
	args1, args2 = args
	print("args1: %r, args2: %r" % (args1, args2))

# two arguments
def print_two_again(args1, args2):
	args1 = args1
	args2 = args2
	print("args1: %r, args2: %r" % (args1, args2))

# one arguments
def print_one(args):
	args = args
	print("args: %r" % args)

# no arguments
def print_none():
	print("I got nothing...")
	
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First")
print_none()