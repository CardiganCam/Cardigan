import os
import time

class sound:

	isPlaying = False
	lastPlayed = int(round(time.time() * 1000))

	def __init__(self):
		self.isPlaying = False



	def play_sound(self, type, urgent):

		self.updateIsPlaying()

		if self.isPlaying == False:
			self.isPlaying = True
			os.system('mpg321 /Users/saoron/cardiganCam/assets/sound/'+str(type)+'.mp3 &')
			self.isPlaying = False

	def updateIsPlaying(self):
		lp =  int(round(time.time() * 1000))

		if int(lp) - int(self.lastPlayed) > 1000:
			self.isPlaying = False
			self.lastPlayed = lp
		else:
			self.isPlaying = True