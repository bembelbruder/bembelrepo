import urllib
import re
import help_fns

regexFilenuke = '<input type="hidden" name="id" value="([^"]*)">\n\s*<input type="hidden" name="fname" value="([^"]*)">'
regexFilenuke2 = "38,'(.*)'\.split"

def base10toN(num,n):
    """Change a  to a base-n number.
    Up to base-36 is supported without special notation."""
    num_rep={10:'a',
             11:'b',
             12:'c',
             13:'d',
             14:'e',
             15:'f',
             16:'g',
             17:'h',
             18:'i',
             19:'j',
             20:'k',
             21:'l',
             22:'m',
             23:'n',
             24:'o',
             25:'p',
             26:'q',
             27:'r',
             28:'s',
             29:'t',
             30:'u',
             31:'v',
             32:'w',
             33:'x',
             34:'y',
             35:'z'}
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 36>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=36:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
            new_num_string=remainder_string+new_num_string
            current=current/n
    return new_num_string


def test(p,a,c,k):
    while c > 1:
        c = c-1
        if k[c]:
            p = re.sub('\\b'+ base10toN(c, 36) +'\\b', k[c], p)

    return p

def getVideoUrl(url):
    data = {'method_free': 'Free'}
    data = urllib.urlencode(data)

    match = help_fns.findAtUrlWithData("var lnk1 = '([^']*)'", url, data)

    scriptMatch = help_fns.findAtUrlWithData('"([^"]*\\.(jpg|png|css|js|css\\?v=1))"', url, data)
    for sm in scriptMatch:
        print sm[0]
        help_fns.openUrl("http://filenuke.com" + sm[0])

    print match[0]
    return match[0]

def getVideoUrl_Outside(url):
    print url
    match = help_fns.findAtUrl("href=['\"](http://filenuke.com/[^'\"]*)['\"]", url)
    print match

    return getVideoUrl(match[0])


def getDownloadCommand():
    return ""