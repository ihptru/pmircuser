#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import socket
import random
import time

import style

class IRC:
    
    def __init__(self, host, port, nickname, msg, target):
        self.irc_host = host
        self.irc_port = port
        self.irc_nick = random.choice(['pm_service'+str(x) for x in range(100)])
        self.nickname = nickname
        self.target = target
        self.msg = msg
        self.irc_sock = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

    def __del__(self):
        self.irc_sock.close()

    def connect(self):
        try:
            self.irc_sock.connect ((self.irc_host, int(self.irc_port)))
        except Exception as e:
            message = ("Error: Could not connect to IRC; Host: %s Port: %s")  % (self.irc_host, self.irc_port) + str(e)
            return message
        str_buff = ("NICK %s \r\n") % (self.irc_nick)
        self.irc_sock.send (str_buff.encode())

        str_buff = ("USER %s 8 * :X\r\n") % (self.irc_nick)
        self.irc_sock.send (str_buff.encode())

        time.sleep(10)

        data = "From "+self.nickname+": "+self.msg
        self.irc_sock.send( (("PRIVMSG %s :%s\r\n") % (self.target, data)).encode() )
        return "Success"


print("""Content-Type: text/html\n""")
content = "<head><title>Private Message to IRC user</title>"
content += "<style>"+style.style+"</style>"
content += """
<script type='text/javascript'>
    function checkInputLength(objTextArea)
    {
        if(this.value.length>100)
        {
            alert('value is too long')
        }
    }
</script>
"""
content += "</head>"

print(content)

f = cgi.FieldStorage()

user = ""
nickname = ""
host = "irc.freenode.net"
port = "6667"
message = ""

messages = ""

everythingSet = True
if "user" in f:
    user = f["user"].value
else:
    everythingSet = False
if "host" in f:
    host = f["host"].value
else:
    everythingSet = False
if "port" in f:
    port = int(f["port"].value)
else:
    everythingSet = False
if "nickname" in f:
    nickname = f["nickname"].value
else:
    everythingSet = False
if "message" in f:
    message = f["message"].value
else:
    everythingSet = False

if (everythingSet):
    irc = IRC(host, port, nickname, message, user)
    messages = irc.connect()
else:
    messages = "All fields are required"

#top
content = "<table class='center' style='margin-top:20px;'><tr><td>Service to send private message to IRC user in any network</td></tr></table>"
print(content)

# text area
content = "<form method=GET action=''>"

content += "<p style='margin-top:20px;'><label for='message'>Your Message</label><br />"
content += "<textarea onKeyUp='checkInputLength(this);' id='message' name='message' rows='5' cols='40' tabindex='4'></textarea>"
content += "<br /><input class='button' type='submit' value='Submit' tabindex='5'/></p>"
print(messages) #warnings etc

content += "<table class='center'>"

content += "<tr><td>Your nickname</td><td><input type='text' name='nickname' value='"+nickname+"'></td></tr>"
content += "<tr><td>Target IRC nickname</td><td><input type='text' name='user' value='"+user+"'></td></tr>"
content += "<tr><td>IRC Server</td><td><input type='text' name='host' value='"+host+"'></td></tr>"
content += "<tr><td>IRC Port</td><td><input type='text' name='port' value='"+port+"'></td></tr>"

content += "</form></table>"

print(content)

