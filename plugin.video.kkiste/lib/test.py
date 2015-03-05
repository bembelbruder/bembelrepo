import urllib
import help_fns
import urlresolver

url = "http://www.movie2k.tl/Stirb-Langsam-4-108104-online-film.html"
regex = '<tr id="tablemoviesindex2" >\\r\\n\\s*.*\\r\\n\\s*\\r\\n\\s*<a href="(.*)">(\\d{2}\\.\\d{2}\\.\\d{4}).*\\r\\n\\s*.*\\r\\n\\s*"16" />&#160;(.*)</a>'

match = help_fns.findAtUrl(regex, url)

print match


