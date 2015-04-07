#Define the imports
import twitch
import logging
import normalMode
import violenceMode
import time
import datetime
import keypresser

keypresser = keypresser.keyPresser()
violence = violenceMode.violenceMode()
normal = normalMode.normalMode()
twitch = twitch.Twitch()
logging.basicConfig(filename='commands.log', level=logging.INFO,format='%(asctime)s - %(message)s', datefmt='%Y/%m/%d %I:%M:%S')
gameStart = True
gameMode = 'normal'
normalMode = 'normal'
democracyMode = 'democracy'
violenceMode = 'violence'
startTime = time.time()
waitTime = 3
cacheCommand = []
execList = []
lastRecvTime = startTime
newMessages = ''

#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
usr = 'easychien';
key = 'oauth:fj8k048zl94xc5l0pn0cvbzwhhscdd'
twitch.twitchConnect(usr, key);



#The main loop
while gameStart:
    #Check for new mesasages
    newMessages = twitch.twitchRecieveMessages()

    #initialize democracy commands
    longestCommand = ['',0]

    if not newMessages:
        #No new messages...
        continue
    else:
        cacheCommand = []
        for message in newMessages:
            
            #Wuhu we got a message. Let's extract some details from it

            msg = message['message'].lower()
            username = message['username'].lower()
            logging.info(username + ': ' + msg + " - GameMode: " + gameMode + " - Run commands/times: " + " - Elapsed time: " + time.strftime('%M:%S', time.localtime(time.time()-startTime)))
            # print(username + ': ' + msg)
            if msg == 'normal' and username == usr:
                gameMode = normalMode
                print('Now normalMode')
                twitch.sendMessage('Now Normal Mode')
                break
            elif msg == 'democracy' and username == usr:
                gameMode = democracyMode
                print('Now democracyMode')
                twitch.sendMessage('Now Democracy Mode')
                break
            elif msg == 'violence' and username == usr:
                gameMode = violenceMode
                print('Now violenceMode')
                twitch.sendMessage('Now Violence Mode')
                break
            elif msg == 'random' and username == usr:
                gameMode = randomMode
                print('Now randomMode')
                twitch.sendMessage('Now Random Mode')
                break

            if msg == 'quit':
            	gameStart = False
            	print('Game stopped, please restart the program!')
            	break
            
            if gameMode == 'normal':
                cacheCommand += normal.count(msg)
            elif gameMode == 'violence':
                temp = violence.countMostCommand(msg)
                if temp[1] > longestCommand[1]:
                    longestCommand[0]=temp[0]
                    longestCommand[1]=temp[1]
            elif gameMode == 'democracy':
                pass

        if gameMode == violenceMode:
        	cacheCommand = longestCommand[0]
        


    if (time.time() - lastRecvTime) >= waitTime:
        # execute
        lastRecvTime = time.time()
        self.initExecCommand()
        execList = cacheCommand
        for i in cacheCommand:
            execCommand[i] += 1
            keypresser.pressKey(i)



def initExecCommand():
    execCommand = {'up': 0,
                'down': 0,
               'left': 0,
               'right': 0,
                 'a': 0,
                 'b': 0,
              'select': 0,
               'start': 0}
    pass




            