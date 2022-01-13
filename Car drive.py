import sys

def on():
	a=input(">>")
	if a=='start':
		print("engine started")
		run()
	elif a=='run':
		print("Engine is off please start")
		on()
	elif a=='stop':
		print("engine is off please start")
		on()
	elif a=="drive":
		print("The car is not started yet please start the car")
		on()
	elif a=="quit":
		print("You have quited")
		sys.exit()
	else:
		print("Invalid command please give a command again")
		on()		
	return started
	


def run():
	a=input(">>")
	if a=='start':
		print("engine already started")
		run()
	elif a=='run':
		print("Engine is running")
		isRunning()
		drive()
	elif a=='stop':
		print("engine is not running please run")
		on()
	elif a=="drive":
		print("The car is not running yet please run the car")
		run()
	elif a=="quit":
		print("You have quited")
		sys.exit()
	else:
		print("Invalid command please give a command again")
		run()


def drive():
	a=input(">>")
	if a=='start':
		print("engine already started")
		run()
	elif a=='run':
		print("Engine is running already")
		drive()
	elif a=='stop':
		 print("enginge stoped")
		 on()
	elif a=="drive":
		print("Car is moving")
		isMoving()
		stop()
	elif a=="quit":
		print("You have quited")
		sys.exit()
	else:
		print("Invalid command please give a command again")
		run()


def stop():
	a=input(">>")
	b=isRunning()
	c=isMoving()
	if a=='start':
		print("engine already started")
		stop()
	elif a=='run':
		print("Engine already is running")
		stop()
	elif a=='stop':
		if c=="moving":
			print("Car stoped")
			print("Engine stoped")
			on()
		elif b=="running":
			print("Engine stoped")
			on()
		else:
			print("Stoped")
	elif a=="drive":
		print("You are driving now")
		stop()
	elif a=="quit":
		print("You have quited")
		sys.exit()
	else:
		print("Invalid command please give a command again")
		stop()
		
def isRunning():
	return "running"
def isMoving():
	return "moving"
on()
