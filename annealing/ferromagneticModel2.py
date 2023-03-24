# 西森教授の論文「Quantum annealing in the transverse Ising model」のⅢのA 強磁性モデル
# Γ(t)は、3/√t

import numpy as np
from qutip import *
import matplotlib.pyplot as plt
import math

nspins = 8 # 8スピン系

# h=0.1, Γ(t)=3/√t
h = 1/10
J = 1/8

sz = [tensor([sigmaz() if i == j else qeye(2) for j in range(nspins)]) for i in range(nspins)]
sx = [tensor([sigmax() if i == j else qeye(2) for j in range(nspins)]) for i in range(nspins)]

# Hcの作成
Hc = 0.
for ispin in range(nspins-1):
    for jspin in range(ispin+1, nspins):
        Hc += - J * sz[ispin] * sz[jspin]

for ispin in range(nspins):
    Hc += -h * sz[ispin]

_, gs_Hc = Hc.groundstate()

# Hqの作成
Hq = -sum(sx)

tau = 1000. # annealing time
def fc(t, args):
    return 1.

def fq(t, args):
    t_new = t + 1
    
    return 3 / math.sqrt(t_new)

#options = Options(nsteps=5000)

H = [[Hc, fc], [Hq, fq]] # total Hamiltonian

H0 = Hc + (3 / math.sqrt(1)) * Hq
_, gs_H0 = H0.groundstate()

tlist = np.arange(0., tau-1, 0.01)
result_sesolve = sesolve(H, gs_H0, tlist, [ket2dm(gs_Hc)])

plt.plot(result_sesolve.times, result_sesolve.expect[0])
plt.xlim(1. , 1000.)
plt.xscale("log")
plt.ylim(0.,1.)
plt.xlabel("t")
plt.ylabel("Probability of GS of Hc")
plt.minorticks_on()
plt.show()