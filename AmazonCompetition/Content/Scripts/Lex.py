import os 

class Lex:
	def begin_play(self):
		ue.log('Starting external voice module')
		os.system(r"START python voice_module\talk.py")
	def tick(self, delta_time):
		pass