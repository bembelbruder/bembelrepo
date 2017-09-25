from lib.hoster.openload import Openload
x = Openload()
link = x.getVideoUrl("https://openload.co/f/IoyTAYVeB2Y")

print link

from lib.sites.kinox import kinox
x = kinox()
x.get