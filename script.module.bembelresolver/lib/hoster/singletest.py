from lib.sites.serienstream.anfangsbuchstaben import Anfangsbuchstaben

s = Anfangsbuchstaben()
s.url = "http://serienstream.to/serien"
for staffel in s.getContent():
    print staffel.name