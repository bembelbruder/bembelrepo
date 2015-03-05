import cgi
import cgitb
import sys
import urlparse

sys.path.append("/home/sascha/.xbmc/addons/script.module.bembelresolver")

import serien

form = cgi.FieldStorage()

print "Content-Type: text/html;charset=utf-8"
print

print "<html>"
print "<head>"
print "</head>"
print "<body>"

url = form.getvalue('url') + "/" + form.getvalue('staff')

s = serien.Serien()
match = s.getFolgen(url)

for m in match:
	print m

print "</body>"
print "</html>"
