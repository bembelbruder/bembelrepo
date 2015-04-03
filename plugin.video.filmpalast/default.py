import sys
import help_fns

from help_fns_xbmc import help_fns_xbmc
from sites.filmpalast import filmpalast

fp = filmpalast.Filmpalast(help_fns_xbmc(int(sys.argv[1])))
fp.handleParameter(help_fns.parameters_string_to_dict(sys.argv[2]))