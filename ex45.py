### Story

### paragraph:
###		a fresh graduate is applying for jobs, he/she first has to to go
### 	through online application channel, phone interview, face2face
### 	interview and offer negotiation. challenges will be real life
###		questions with funny ways to die (start again)

### Scene:

### Rejection scene - this is when the player got rejected and should be 	 something funny/encouraging
### Home scene - this is starting point and as procrastination already 		showed up, the player need to defeat it before continuing
### Online Scene - where the player apply jobs online, he/she must 			answer basic questions correctly before continuing
### Phone Scene - where the player gets phone interview, he/she must 		answer basic questions correctly
### Office Scene - where the player gets face to face interview, he/she 	must answer basic questions correctly and tell a joke before 			continuing
### Offer Scene - where player gets the offer after he/she decide 			whether to ask for pay raise, accept or decline


### Key Concept
#	Player
#

from sys import exit
from random import randint
import random

class Scene(object):

	def enter(self):
		print "This scene has some issue, Subclass it and implement enter()"
		exit(1) # Means having issues

class Engine(object):
	"""docstring for Engine"""
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:

			print "\n-------------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Reject(Scene):
	quips = [
			"You failed. You kinda suck at this.",
			"You are out! Wrap up your tears and try later.",
			"You were so close! How can you do differently?",
			"You failed to impress the boss."
		]

	def enter(self):
		print Reject.quips[randint(0, len(self.quips)-1)]
		exit(1)


class Online(Scene):
	"""docstring for Home"""
	print "What can I call you?"
	name = raw_input(">")

	def enter(self):
		print "Welcome %s!" % Online.name
		print "\n"
		print "You have just graduated from the Ivory league and looking"
		print "for a job. After a late night drink from your graduation"
		print "party, you woke up at 3pm and decide to apply for jobs"
		print " tomorrow."
		print "\n"
		print "You are now sitting in front of your laptop and opened"
		print "your Linkedin job search page. A job search notification"
		print "pop up and your dream job is hiring. What would you do?"

		action = raw_input(">")

		if action == "apply":
			print "You click on the link and go through the JD. It seemed"
			print "like a tailored job for you."
			print "You click the apply button and start filling in details."
			print "After going through 10 pages of questions, you finally"
			print "get to the submit page. It is just one step away from your"
			print "dream, would you like to proceed?"

			action2 = raw_input(">")

			if action2 == "yes":
				print "Your details has been successfully submitted. Now is"
				print "You can sit and wait."
				return 'phone'
			else:
				print "Your session has expired, try again."
				return 'online'
		else:
			print "DOES NOT COMPUTE"
			return 'online'


class Phone(Scene):
	"""docstring for Home"""
	def enter(self):
		print "Congratulations %s! You made it to the phone interview!" % Online.name
		print "The hiring manager Maria really liked your background and"
		print "decide to give you a call."
		print "She want to know more about how you solve problems:"
		print "How many M&M chocolate beans sold every year?"
		print "Hint: minimum number is 10,000. Increased by 10,000. You have 10 chances."

		code = random.randint(1,9)*10000
		guesses = 1

		while True:
			guess1 = raw_input("Please enter a number: ")
			try:
				guess = int(guess1)
			except ValueError:
				print "You didn't enter a number"
				continue



			if guess != code and guesses < 11:
				print "This is your %d try, you might want to guess again. " % guesses
				#print "%s" %code
				guesses += 1
				continue

			if guess == code:
				print "Maria was impressed. You are one step closer to getting"
				print "this job!"
				print "Now comes your next challenge, she invited you to the"
				print "face to face interview in office tomorrow morning."
				print "Get some rest and prepare well!"
				return 'office'

			else:
				print "Time's up, Maria hung up the phone and not pleased about"
				print "how she can better utilise her time."
				return 'reject'

class Office(Scene):
	"""docstring for Home"""
	def enter(self):
		print "You made it to the second round, you must be so proud!"
		print "Maria's manager Bob welcomed you by introducing himself,"
		print "He seems like an easygoing guy."
		print "You spent the next 30 mins selling your skills and dreams,"
		print "Bob looks really interested. Now it is your chance to impress"
		print "him with one last questions."
		print "What would you ask?"
		print "1. Why he joined the company."
		print "2. What reason is the last member left if this position is not new."
		print "3. What is his favorite sports."
		print "Type the number of your choice:"
		question = raw_input("[keypad]>")

		if question == "1":
			print "Bob enjoys to recall the adventure when he joined. He talked for"
			print "half an hour until someone else knocked on the door and kick you"
			print "two out of the meeting room. He shakes your hand sincerely and"
			print "say keep in contact."
			return 'offer'

		elif question == "2":
			print "This role is newly set up so they are recruiting for someone"
			print "who can bring the difference."
			return 'reject'

		elif question =="3":
			print "Bob likes basketball and is a fan of Bulls, too sad you put"
			print "your fav Heat team in your resume as hobbies!"
			return 'reject'

		else:
			print "TRY AGAIN. Type in the numbers 1, 2 or 3."
			return 'office'

class Offer(Scene):
	"""docstring for Home"""
	def enter(self):
	    salary = 100*randint(10,90)
	    print "Congratulations %s, Bob and Maria both satisfied with your expertise" % Online.name
	    print "and want to welcome you to the team. They decide to offer you %d" %salary
	    print "as monthly salary, would you like to proceed?"
	    response = raw_input(">")

	    if response == "yes":
	    	print "Congratulations, you got the job! now is time to celebrate with"
	    	print "your friend and get drunk again before your day in and day out routine!"
	    	print "/n"
	    	exit(1)

	    elif response == "higher salary":
	    	print "You greedy pig. Bob and Maria start to think they are making the"
	    	print "wrong decision. Try AGAIN!"
	    	return 'offer'

	    else:
	    	print "You know what is the current unemployment rate? Go back to your part-"
	    	print "time job at Wendy's and keep washing dishes!"
	    	return 'online'

class Map(object):

	scenes = {
		'online': Online(),
		'phone': Phone(),
		'office': Office(),
		'offer': Offer(),
		'reject': Reject(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
 		return self.next_scene(self.start_scene)

a_map = Map('online')
a_game = Engine(a_map)
a_game.play()