import random
nice_comment = ["Nice name!", "Congratulations on discovering a planet!", "See you soon!", "Thank you for your contributions.", "You have furthered humanity's width of understanding of the Galaxy!That is something to be proud of!", "Thank you, and Have a nice day!"]
print ("Welcome to the Dashboard. Our goal is to enhance your map of the galaxy.")
dashboard = {}

def create_map():
	add_planet()
	
def add_planet():
	planet = input ("Type name of new planet:")
	position_of_planet = input ("What is the position of " + planet + ". Please scale to the Gargaw unit.")
	dashboard[planet] = position_of_planet
	
def update_position():
	planet = input ("Which planet would you like to update? ")
	if planet in dashboard:
		position_of_planet = input("New position? Unit should be in Gargaw: ")
		dashboard[planet] = position_of_planet
	else:
		print("Undefined planet")
		
def delete_planet():
	del dashboard[planet]
	
def print_planet_dictionary():
	length_of_nice_comment = len(nice_comment)
	random_index = random.randint(0, length_of_nice_comment-1)
	print(dashboard[random_index])
	
	
while done = 1
print("Do you want to a. add a planet, b. update its position, c. delete a planet, or d. view the planet dictionary?")
choice1 = input("Type a, b, c, or d: ")
	if choice1 == "a":
		add_planet()
		print_planet_dictionary()
		a = input("Done? Type yes or no: ")
		if a == "yes":
			done = done + 1
	elif choice1 == "b":
		update_position()
		print_planet_dictionary()
		b = input("Done? Type yes or no: ")
		if b == "yes":
			done = done + 1
	elif choice1 == "c":
		delete_planet()
		print_planet_dictionary()
		c = input("Done? Type yes or no: ")
		if c == "yes":
			done = done + 1
	elif choice1 == "d":
		print_planet_dictionary()
		d = input("Done? Type yes or no: ")
		if d == "yes":
			done = done + 1
	else:
		print ("error")
		e = input("Done? Type yes or no: ")
		if e == "yes":
			done = done + 1

	