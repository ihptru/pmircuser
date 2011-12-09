#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi, os
import style

print("""Content-Type: text/html\n""")
content = "<head><title>Private Message to IRC user</title>"
content += "<style>"+style.style+"</style>"
content += "</head>"

print(content)

f = cgi.FieldStorage()
user = ""

if "user" in f:
    user = f["user"].value

content = "<table class='center'>"

content += "<form method=GET action=''>"
content += "<tr><td>Your nickname (optional)</td><td><input type='text' name='nickname'></td></tr>"
content += "<tr><td>Target IRC nickname</td><td><input type='text' name='target' value='"+user+"'></td></tr>"
content += "<tr><td>IRC Server</td><td><input type='text' name='server' value='irc.freenode.net'></td></tr>"
content += "<tr><td>IRC Port</td><td><input type='text' name='server' value='6667'></td></tr>"

# text area
content += "<label for='message'>Your Message</label><br />"
content += "<textarea id='message' name='message' rows='10' cols='40' tabindex='4'></textarea>"
content += "</p>"
content += "<p class='no-border' style='text-align:center'>"
content += "<input class='button' type='submit' value='Submit' tabindex='5'/>"
content += "</p>"

content += "</form></td></tr></table>"

print(content)

