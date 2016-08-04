import random

five_syllables = ["Breathtakingly nice", "Juggle fire and ice", "Don't you ever dare mess", "My toungue is tangled", "Why art thou weary", "Blistering paper", "Summer is coming", "Release is not near", "Need coldness here", "I am not dying"]
seven_syllables = ["Dragons fly through the night sky", "The stream flows through the dark woods", "Light shines off shiny objects", "Rain falls softly on the ground", "Bright red lights illuminate", "Majestic trees stand above", "Sadness seeps through the heart's cracks", "The sun blazes through my skin", "The water rises to me", "Tingling and shuddering"]

for i in range(3):
	five_length = len(five_syllables)
	random_index5a = random.randint(0, five_length-1)
	print (five_syllables[random_index5a])
	
	seven_length = len(seven_syllables)
	random_index7 = random.randint(0, seven_length - 1)
	print(seven_syllables[random_index7])
	
	random_index5b = random.randint(0, five_length-1)
	print(five_syllables[random_index5b])
	
	print("")