class violenceMode:

	def countMostCommand(self,message):
		self.initializeCount()
		mostCommand = ['',0]
		for command in message.split():
			for commandLength in range(1,7):
				for count in range(0,len(command),commandLength):
					if (count+commandLength)<=len(command):
						if  (commandLength == 1) and (command[count:count+commandLength] == 'a'):
							if  command[count:count+3] != 'art':
								self.countCommand['a'] += 1
						if  (commandLength == 1) and (command[count:count+commandLength] == 'b'):
							self.countCommand['b'] += 1
						if  (commandLength == 2) and (command[count:count+commandLength] == 'up'):
							self.countCommand['up'] += 1
						if  (commandLength == 4) and (command[count:count+commandLength] == 'down'):
							self.countCommand['down'] += 1
						if  (commandLength == 4) and (command[count:count+commandLength] == 'left'):
							self.countCommand['left'] += 1
						if  (commandLength == 5) and (command[count:count+commandLength] == 'right'):
							self.countCommand['right'] += 1
						if  (commandLength == 5) and (command[count:count+commandLength] == 'start'):
							self.countCommand['start'] += 1
						if  (commandLength == 6) and (command[count:count+commandLength] == 'select'):
							self.countCommand['select'] += 1

		for c in self.countCommand.keys():
			if self.countCommand[c] > mostCommand[1]:
				mostCommand[0] = c
				mostCommand[1] = self.countCommand[c]

		return mostCommand



	def initializeCount(self):
		for i in self.countCommand.keys():
			self.countCommand[i]=0

	def __init__(self):
		self.countCommand = {'up': 0,
                    		'down': 0,
             		       'left': 0,
             		       'right': 0,
           			         'a': 0,
           			         'b': 0,
          		          'select': 0,
          			       'start': 0}




