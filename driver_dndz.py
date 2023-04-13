from importlib import reload

import universe
reload(universe)
from universe import *

import projection_kernel
reload(projection_kernel)
from projection_kernel import *

import latex
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

from matplotlib.pyplot import figure

##################################################################################

u = UnivPlanck15()


# various projection kernels
w_cmblens = WeightLensSingle(u, z_source=1100., name="cmblens")
w_gallens = WeightLensSingle(u, z_source=1., name="gallens")
w_y = WeightY(u)
w_cib545 = WeightCIBPenin12(u, nu=545.e9, fluxCut=350.e-3)


# CMASS, WISE
w_cmass = WeightTracerCMASS(u)
w_wise = WeightTracerWISE(u)
# plot
#wArr = [w_cmass, w_wise]
#w_wise.plotDndz(wArr, logy=True)

# LSST
w_lsstgold = WeightTracerLSSTGold(u)
w_lsstsources = WeightTracerLSSTSourcesDESCSRDV1(u)
# plot
#wArr = [w_lsstgold, w_lsstsources]
#w_lsstgold.plotDndz(wArr, logy=True)

# DESI
w_desibgs = WeightTracerDESIBGS(u)
w_desilrg = WeightTracerDESILRG(u)
w_desielg = WeightTracerDESIELG(u)
w_desiqso = WeightTracerDESIQSO(u)
# plot
#wArr = [w_desibgs, w_desilrg, w_desielg, w_desiqso]
#w_desibgs.plotDndz(wArr, logy=True)

# SPHEREx
w_spherex01234 = WeightTracerSPHEREx(u, ISample=[0,1,2,3,4])
w_spherex0 = WeightTracerSPHEREx(u, ISample=[0])
w_spherex1 = WeightTracerSPHEREx(u, ISample=[1])
w_spherex2 = WeightTracerSPHEREx(u, ISample=[2])
w_spherex3 = WeightTracerSPHEREx(u, ISample=[3])
w_spherex4 = WeightTracerSPHEREx(u, ISample=[4])
# plot
#wArr = [w_spherex0, w_spherex1, w_spherex2, w_spherex3, w_spherex4, w_spherex01234]
#w_spherex0.plotDndz(wArr, logy=True)

# plot them all
wArr = [w_desibgs, w_desilrg, w_desielg, w_desiqso]
wArr += [w_cmass, w_wise, w_lsstgold, w_lsstsources]
wArr += [w_spherex01234]
w_desibgs.plotDndz(wArr, logy=True)





