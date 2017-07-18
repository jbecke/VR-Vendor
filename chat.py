# twich chat bot
# python3
# By Jacob Beckerman, jbecke at seas dot upenn dot edu
import socket
from time import sleep
HOST = "irc.twitch.tv"              # the Twitch IRC server
PORT = 6667                         # always use port 6667!
NICK = "jbecke"            # your Twitch username, lowercase
PASS = "oauth:qpjihb9a9c75lcyd10k0dipegt9s8v" # your Twitch OAuth token
CHAN = "jbecke"                   # the channel you want to join

def chat(sock, msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    sock.send("PRIVMSG #{} :{}\r\n".format(CHAN, msg).encode("utf-8"))

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
counter = 0
'''
while counter < 20:
    response = s.recv(1024).decode("utf-8")
    print(response)
    sleep(0.2)
    counter = counter + 1
'''
response = s.recv(1024).decode("utf-8")
print(response)
chat(s, "jbecke purchased: Ancient Silver Sword ||| Damage: 375 per hit ||| Critical: ||| 925 ||| Critical chance: 15%")
chat(s, "   ^^^ BUY THIS ITEM ^^^ goo.gl/atAEou")
s.close()