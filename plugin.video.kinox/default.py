import sys
import help_fns

from help_fns_xbmc import help_fns_xbmc
from sites.kinox.kinox import Kinox

kx = Kinox(help_fns_xbmc(int(sys.argv[1])))
kx.handleParameter(help_fns.parameters_string_to_dict(sys.argv[2]))