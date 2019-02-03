import scipy
import matplotlib.pyplot as plt
import numpy
from os.path import join
from mayavi import mlab
from scipy.io import loadmat

datadir = "core1 2 3-20190201T183913Z-001"
subdir  = "core1 2 3"
rho1 = loadmat(join(join(datadir, subdir), 'rho1.mat' ))
bi = loadmat(join(join(datadir, subdir), 'bi1.mat' ))
bj = loadmat(join(join(datadir, subdir), 'bj1.mat' ))
bk = loadmat(join(join(datadir, subdir), 'bk1.mat' ))


mlab.contour3d(rho1['cl'])
mlab.flow(bk['bk'],bj['bj'],bi['bi'])
