from hoster import ecostream
from hoster import filenuke
from hoster import movshare
from hoster import played
from hoster import streamcloud
from hoster import videoweed
from hoster import vidstream
from hoster import youwatch
from hoster.FileNotExistsException import FileNotExistsException

ecostreamUrls = ["http://www.ecostream.tv/stream/36e964d02e42774e9105a5a60c794397.html"]
filenukeUrls = ["http://filenuke.com/yctpsoif70tm"]
movshareUrls = ["http://www.movshare.net/video/86ce1b3398a19"]
playedUrls = []
streamcloudUrls = ["http://streamcloud.eu/8zdaml5v8t5a/NCIS.S11E13.Gueterzug.nach.Miami_Ger_Dub__BB_.avi",
                   "http://streamcloud.eu/3ib23h67by11/dzckl00.mkv.html"]
videoweedUrls = ["http://www.videoweed.es/file/efa245a19981b"]
vidstreamUrls = ["http://vidstream.in/lz81rjcimtn9"]
youwatchUrls = ["http://youwatch.org/vg0r29saj0zo"]

def checkHoster(pHosterName, pHoster, pUrls):
    try:
        for url in pUrls:
            pHoster.getVideoUrl(url)
    except FileNotExistsException:
        print pHosterName + ": Datei existiert nicht: " + url
    except:
        print pHosterName + " funktioniert nicht"

checkHoster("Ecostream", ecostream, ecostreamUrls)
checkHoster("Filenuke", filenuke, filenukeUrls)
checkHoster("Movshare", movshare, movshareUrls)
checkHoster("Played", played, playedUrls)
checkHoster("Streamcloud", streamcloud, streamcloudUrls)
checkHoster("Videoweed", videoweed, videoweedUrls)
checkHoster("Vidstream", vidstream, vidstreamUrls)
checkHoster("Youwatch", youwatch, youwatchUrls)
