import sys
import help_fns

from help_fns_xbmc import help_fns_xbmc
from sites.kkiste import kkiste

kk = kkiste.KKiste(help_fns_xbmc(int(sys.argv[1])))
kk.handleParameter(help_fns.parameters_string_to_dict(sys.argv[2]))