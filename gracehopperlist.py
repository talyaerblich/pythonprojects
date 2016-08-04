grace_hopper = []
grace_hopper.extend(["Holia", "Francesca", "Talya", "Ann", "Gloria"])
grace_hopper.remove("Ann")
grace_hopper.insert(2, "Dewan")
grace_hopper.pop(len(grace_hopper)-1)
grace_hopper[3] = "Abigail"
#print(grace_hopper)
for student in grace_hopper:
	print (student)
print(len(grace_hopper))