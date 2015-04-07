class normalMode:

	def count(self,message):
		command = []
		for command in message.split():
			for commandLength in range(1,7):
				for count in range(0,len(command),commandLength):
					if (count+commandLength)<=len(command):
						if  (commandLength == 1) and (command[count:count+commandLength] == 'a'):
							if  command[count:count+3] != 'art':
								command.append('a')
								# keypresser.pressKey('a')
						if  (commandLength == 1) and (command[count:count+commandLength] == 'b'):
							command.append('b')
							# keypresser.pressKey('b')
						if  (commandLength == 2) and (command[count:count+commandLength] == 'up'):
							command.append('up')
							# keypresser.pressKey('up')
						if  (commandLength == 4) and (command[count:count+commandLength] == 'down'):
							command.append('down')
							# keypresser.pressKey('down')
						if  (commandLength == 4) and (command[count:count+commandLength] == 'left'):
							command.append('left')
							# keypresser.pressKey('left')
						if  (commandLength == 5) and (command[count:count+commandLength] == 'right'):
							command.append('right')
							# keypresser.pressKey('right')
						if  (commandLength == 5) and (command[count:count+commandLength] == 'start'):
							command.append('start')
							# keypresser.pressKey('start')
						if  (commandLength == 6) and (command[count:count+commandLength] == 'select'):
							command.append('select')
							# keypresser.pressKey('select')
		
		return command
		