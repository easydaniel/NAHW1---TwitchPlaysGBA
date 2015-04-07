import socket
import sys
import re

class Twitch:

    user = ""
    oauth = ""
    s = None

    def twitchLoginStatus(self, data):
        if not re.match(r'^:(testserver\.local|tmi\.twitch\.tv) NOTICE \* :Login unsuccessful\r\n$', data): return True
        else: return False

    def twitchConnect(self, user, key):
        self.user = user
        self.oauth= key
        print("Connecting to twitch.tv")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connectHost = "irc.twitch.tv"
        connectPort = 6667
        try:
            s.connect((connectHost, connectPort))
        except:
            print("Failed to connect to twitch")
            sys.exit()
        print("Connected to twitch")
        print("Sending our details to twitch...")
        s.send(('USER %s\r\n' % user).encode())
        s.send(('PASS %s\r\n' % key).encode())
        s.send(('NICK %s\r\n' % user).encode())

        if not self.twitchLoginStatus(s.recv(1024).decode()):
            print("... and they didn't accept our details")
            sys.exit()
        else:
            print("... they accepted our details")
            print("Connected to twitch.tv!")
            self.s = s
            s.send(('JOIN #%s\r\n' % user).encode())
            s.recv(1024).decode()

    def sendMessage(self,message):
        self.s.send(('PRIVMSG #%s : %s\r\n' % (self.user,message)).encode())
        pass        

    def checkHasMessage(self, data):
        return re.match('^:([a-zA-Z0-9_]+)\!([a-zA-Z0-9_]+)@([a-zA-Z0-9_])+(\.tmi\.twitch\.tv|\.testserver\.local) PRIVMSG #([a-zA-Z0-9_]+) :(.+)$', data)

    def parseMessage(self, data):
        return {
            'channel': re.findall('^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', data)[0],
            'username': re.findall('^:([a-zA-Z0-9_]+)\!', data)[0],
            'message': re.findall('PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0]
        }

    def twitchRecieveMessages(self, amount=1024):
        data = None
        try:
            data = self.s.recv(1024).decode()
        except: return False

        if not data:
            print("Lost connection to Twitch, attempting to reconnect...")
            self.twitchConnect(self.user, self.oauth)
            return None

        #self.ping(data)

        if self.checkHasMessage(data):
            return [self.parseMessage(line) for line in filter(None, data.split('\r\n'))]