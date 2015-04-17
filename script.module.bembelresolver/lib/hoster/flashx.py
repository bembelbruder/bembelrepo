import help_fns
import re
import cookielib
import urllib
import urllib2
import time

from hoster.BaseHoster import BaseHoster

class Flashx(BaseHoster):
    pass

    def getName(self, link, name):
        return re.compile('name="' + name + '" value="([^"]*)"').findall(link)
    
    def getVideoUrl(self, url):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        headers = [('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                   ('Accept-Encoding', 'none'),
                   ('Accept-Language', 'en-US,en;q=0.5'),
                   ('Host', 'www.flashx.tv'),
                   ('Connection', 'keep-alive'),
                   ('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:37.0) Gecko/20100101 Firefox/37.0'),
                   ]
        opener.addheaders = headers
        req = urllib2.Request(url)
        link = opener.open(req).read()
        url = "http://www.flashx.tv" + re.compile("action='([^']*)'").findall(link)[0]
        op = self.getName(link, "op")
        myid = self.getName(link, "id")
        fname = self.getName(link, "fname")
        myhash = self.getName(link, "hash")
        referer = self.getName(link, 'referer')
        
        data = {"op": op, "id": myid, "fname": fname, "hash": myhash, "referer": referer, "usr_login": "", "imhuman": "Proceed to video"}
        data = urllib.urlencode(data)
        for c in cj:
            print c
        time.sleep(7)
        print opener.open(url, data).read()
# <script type='text/javascript'>eval(function(p,a,c,k,e,d){while(c--)if(k[c])p=p.replace(new RegExp('
# \\b'+c.toString(a)+'\\b','g'),k[c]);return p}('c("3c").3b({3a:[{f:"4://9.3.2/39.38"},{f:"4://t-s.3.2
# /37/36.35"}],34:"4://t-33.3.2/i/s/32/31.30",2z:"2y",q:2x,p:2w,2v:"2u",2t:"2s",2r:"2q 2p 2o.2",2n:"4:
# //9.3.2/7.8",r:{f:"4://2m.3.2/r/2l.2k",n:"4://9.3.2/7.8",j:"2j"},2i:"2h",2g:[],2f:{2e:\'#2d\',2c:15,2b
# :"2a",29:0},"28":{27:"%26 25%6%24%23%21%20.3.2%1z-7-1y.8%22 1x%6%e%22 1w%6%e%22 1v%6%e%22 1u%6%1t%22
#  q%6%1s%22 p%6%1r%22%o%1q%1p%o",n:"4://9.3.2/7.8"},1o:{1n:"7",1m:"1l-1k-1j.1i"},1h:{1g:5}});d b;d 1f
# =0;d 1e=0;c().1d(a(x){m(x)});c().1c(a(){$(\'l.k\').1b()});a m(x){$(\'l.k\').j();1a(b)19;b=1;$.18(\'4
# ://9.3.2/h-17/16.h?14=13&12=7&11=10-z-y-w-v\',a(g){$(\'#u\').8(g)})}',36,121,'||tv|flashx|http||3D|k7szezxcdeh9
# |html|www|function|vvplay|jwplayer|var|220|file|data|cgi||hide|video_ad|div|doPlay|link|3E|height|width
# |logo|01|hyxe1|fviews|0e38e79302d2c46a8eec19734aee2aaf|1428837437||59|84|467811|hash|file_code|view|op
# ||index_dl|bin|get|return|if|show|onComplete|onPlay|p0467811|tt467811|bufferlength|rtmp|mkv|sd|maennerhort
# |exq|idstring|label|ga|2Fiframe|3C|22272|22640|22no|scrolling|marginheight|marginwidth|frameborder|640x272
# |2Fembed|2Fwww|2F||3A|22http|src|3Ciframe|code|sharing|backgroundOpacity|Verdana|fontFamily|fontSize
# |FFFFFF|color|captions|tracks|start|startparam|true|png|watermark|static|aboutlink|flashX|by|Powered
# |abouttext|stormtrooper|skin|flash|primary|272|640|5872|duration|jpg|v5jgvcr3azxt|00093|thumb|image|mp4
# |video1|luq4q2wee3ixexzw6uvlfz6sqx5cphsgtvk5wlcmlndccucuhz4egngcwu6a|smil|luq4q2wee3ixexzw6uvlfz6sqx5cphsgtvk5wlcmkqnccucuhz4lbboryypa
# |sources|setup|vplayer'.split('|')))
# </script>