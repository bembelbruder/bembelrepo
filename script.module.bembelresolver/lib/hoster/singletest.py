from lib.hoster.powerwatch import Powerwatch
from lib.sites.serien.hoster import Hoster

h = Hoster()
h.init("https://bs.to/serie/Navy-CIS/13/23-Toedlicher-Wettlauf/Vidto-1", 'Vidto', 'test')
print h.getVideoUrl()
