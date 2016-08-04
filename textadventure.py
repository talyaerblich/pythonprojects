start = '''
You awaken in an unfamiliar place. 
There's something under the snow in front of you.
You wipe off the snow. 
Before you is a plaque on a hatch reading: "STARKILLER BASE". Subtle.
To your left is a building. 
Looming in front of you is a forest. 
The hatch is at your feet. 
'''
error = '''
You failed at typing. Cheaters never prosper. You die.
END.
'''

outcome_1 = '''
You are in the building for about 5 seconds when you're intercepted by a woman named Captain Phasma.
"SEIZE HER!", she orders. 
You are handcuffed and marched away. 
They deliver you to a drab looking cell, and proceed to inform you that you can stay in the cell for the rest of your "miserable existence" or you can join the Stormtrooper forces.
END.
'''
outcome_1a = '''
You are condemned to live with alien rats in a lonely cell for the rest of your life.
The good thing is, your life doesn't last too long because that day the Resistance blows up the entire base.
END.
'''
outcome_1b = '''
You get a super cool uniform and are just about to start your tour of the facility, when everything around you (including you) is reduced to dust by a Resistance-created explosion.
END.
'''
outcome_2 = '''
You yank open the hatch and clamber inside. 
Too late, you realize you forgot to wipe the snow off the part of the hatch labeled: "GARBAGE DISPOSAL CHUTE"
You are given the liberty of choosing your death.
Mysterious garbage serpent or the walls slowly crushing you?
'''
outcome_3 = '''
You enter the forest in a blizzard. 
With your impaired vision, you can make out two paths. 
Right or left?
'''
outcome_3a = '''
You go down the left path. 
Ahead you see two figures arguing with each other.
You clear your throat, and they both look up simultaneously.
Thankfully, the two figures turn out to be Rey and Finn, Resistance fighters.
They invite you to take cover in the Milennium Falcon until they make their escape.
You aren't sure what to say.
They might need your help, but the ship would guarantee your safety.
Insist on staying with them, or head to the ship?
'''
outcome_3ai= '''
Just as you open your mouth to insist on staying with them, a group of Stormtroopers swarm out from behind the trees. 
Rey tries her best to protect the three of you with her lightsaber, but it is too late for you.
The most you can do as a fatal laser strikes your chest is wish Rey and Finn luck in their endeavor.
END.
'''
outcome_3aii = '''
You dash to the ship, and eventually Rey and Finn return safely.
You join their crew and explore the galaxy with them until one planet strikes you with a sense of familiarity.
You've found your home! Congratulations!
You decide to stay there and live out the rest of your long life happily.
END.
'''
outcome_3b = '''
An imposing figure approaches you as you walk down the path. 
"WHO'S THERE?" calls the angered voice of none other than Kylo Ren.
Approach him or run?
'''
outcome_3bi = '''
Trembling with fear, you turn and dash deep into the forest in a random direction.
Eventually you die of hypothermia because the authors lost time and patience.
END.
'''
outcome_3bii = '''
You keep moving forward.
Kylo Ren whips out his lightsaber and holds it to your neck.
"I have a proposition for you." He says. "Either find  a robot called BB8 and bring it to me or die"
Will you accept his proposition?
'''
outcome_3baii1 = '''
"I will never work for you!" You scream. 
He smiles a lipless smile and draws the lightsaber across your throat. 
Everything goes dark.
END.
'''
outcome_3bii2 = '''
"Why not?" You say."I'll find BB8."
You continue walking down the path until you stumble upon an orange droid... and its two companions.
They are distracting themselves by arguing, so you attempt to steal BB8.
BB8 whines loudly and the girl notices you immediately.
"Who is this, Rey?" Asks the man.
"That's none of your concern," you say, "I'm taking this droid and you can't stop me."
"Not on my watch." Rey growls.
She raises her lightsaber to fend you off, you freak out, having come close to death several times today, and run backwards.
When you turn to look where you're going, you realize there's no ground where your feet are.
It's a very cartoon moment, to be honest, as you fall into a large crack in the earth.
END.
'''
x = 0
print("You have 5 attempts to complete your journey successfully. Each failed attempt starts you over at the beginning until you run out of attempts. Good luck, and try not to die.")
while x <= 5:
	print (start)
	print("Where would you like to go? Type 'building', 'forest', or 'hatch'.")
	user_input = input()
	if user_input == "building":
		print(outcome_1 + "What do you choose? Type 'cell' or 'join'.")
		user_input2 = input()
		if  user_input2 == "cell":
			print(outcome_1a)
			x+=1
		elif user_input2 == "join":
			print(outcome_1b)
			x+=1
		else:
			print(error)
			x+=1
	elif user_input == "hatch":
		print(outcome_2 + "Which death do you prefer? Type 'serpent' or 'crushed'.")
		user_input3 = input()
		print('THE END')
		x+=1
	elif user_input == "forest":
		print(outcome_3 + "Type 'right' or 'left'.")
		user_input4= input()
		if user_input4 == "left":
			print (outcome_3a + "Type 'stay' or 'ship'.")
			user_input5 = input()
			if user_input5 == "stay":
				print(outcome_3ai)
				x+=1
			elif user_input5 == "ship":
				print(outcome_3aii)
				x+=1
			else: 
				print(error)
				x+=1
		elif user_input4 == "right":
			print (outcome_3b + "Type 'approach' or 'run'.")
			user_input6 = input()
			if user_input6 == "run":
				print(outcome_3bi)
				x+=1
			elif user_input6 == "approach":
				print(outcome_3bii + "Type 'accept' or 'deny.")
				user_input7 = input()
				if user_input7 == "deny":
					print(outcome_3baii1)
					x+=1
				elif user_input7 == "accept":
					print(outcome_3bii2)
					x+=1
				else: 
					print(error)
					x+=1
			else:
				print(error)
				x+=1
		else:
			print(error)
			x+=1
	else:
		print(error)
		x+=1
print("You died too many times. Now you have no more attempts.")
	
				
	
	
	
	
	