class normalMode:

	def count(self,message):
		execCommand = []

		for command in message.split():
			for commandLength in range(1,7):
				for count in range(0,len(command),commandLength):
					if (count+commandLength)<=len(command):
						if  (commandLength == 1) and (command[count:count+commandLength] == 'a'):
							if  command[count:count+3] != 'art':
								execCommand.append('a')
								# keypresser.pressKey('a')
						if  (commandLength == 1) and (command[count:count+commandLength] == 'b'):
							execCommand.append('b')
							# keypresser.pressKey('b')
						if  (commandLength == 2) and (command[count:count+commandLength] == 'up'):
							execCommand.append('up')
							# keypresser.pressKey('up')
						if  (commandLength == 4) and (command[count:count+commandLength] == 'down'):
							execCommand.append('down')
							# keypresser.pressKey('down')
						if  (commandLength == 4) and (command[count:count+commandLength] == 'left'):
							execCommand.append('left')
							# keypresser.pressKey('left')
						if  (commandLength == 5) and (command[count:count+commandLength] == 'right'):
							execCommand.append('right')
							# keypresser.pressKey('right')
						if  (commandLength == 5) and (command[count:count+commandLength] == 'start'):
							execCommand.append('start')
							# keypresser.pressKey('start')
						if  (commandLength == 6) and (command[count:count+commandLength] == 'select'):
							execCommand.append('select')
							# keypresser.pressKey('select')
		# print(execCommand)
		return execCommand
		