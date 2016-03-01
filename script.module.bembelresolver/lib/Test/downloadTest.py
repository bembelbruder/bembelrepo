from lib.sites.serien.serie import Serie

s = Serie()
s.init("http://bs.to/serie/Bibi-und-Tina")
staffel = s.getStaffel(1)
folge = staffel.getContent()[1]
folge.url = "http://bs.to/" + folge.url
folge.displayName = "Bibi_und_Tina_01_01"
folge.download()