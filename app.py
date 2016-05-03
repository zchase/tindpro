import pynder, time

facebook_id = "100006207555525"
facebook_auth_token = "EAAGm0PX4ZCpsBADvj0npqtdWS74kjtZAUOqeDjB0HHsDEq05JLGQOqtirrfyNMaw31IKN9gEVDQH6mW5qfHCROwIFgoY8Er3V60qtimW2biHDAm8lvdrVAKns60IIT8Cii6qooF47Bg94veeOZCTCK58NnkksCbRZBZBD7p5T2wZDZD"
session = pynder.Session(facebook_id, facebook_auth_token)
#session.profile  # your profile. If you update its attributes they will be updated on Tinder.

def like():
	users = session.nearby_users(limit=100)
	for user in users:
		if user.like():
			user.message('Hey Tinder messaging is beyond messed up on my phone and I think you are really cute! I am kinda hesitant to just give out my phone number (I am sure you understand), so add me on snapchat: zackchase824 :)')
		else:
			print "no match bitch"

def likeLoop():
	for x in range(0, 10000):
		matchMessage()
		time.sleep(5)
		like()

def matchMessage():
	matches = session.matches()
	for match in matches:
		if len(match.messages) == 0:
			match.message('Hey Tinder messaging is beyond messed up on my phone and I think you are really cute! I am kinda hesitant to just give out my phone number (I am sure you understand), so add me on snapchat: zackchase824 :)')
			print "message sent"

likeLoop()