import numpy as np
from qutip import *
import matplotlib.pyplot as plt
import random

Jzz = {(0,1): 0.8} # 相互作用
hz = {0: 0.2, 1:1.2} # 局所磁場

#スピン演算子の準備
sz = [tensor([sigmaz() if i == j else qeye(2) for j in range(2)]) for i in range(2)]
sx = [tensor([sigmax() if i == j else qeye(2) for j in range(2)]) for i in range(2)]

# Hc作成
Hc = -Jzz[(0,1)] * sz[0] * sz[1]
for isite in range(2):
    Hc += -hz[isite] * sz[isite]

# Hq作成
Hq = -sum(sx)

# 0から1までを0.01づつ
slist = np.linspace(0.0, 1.0, 101)
Englists = [[] for _ in range(2**2)]

for s in slist:
    H = s * Hc + (1.-s) * Hq
    eigvals = H.eigenenergies()
    for ilevel in range(2**2):
        Englists[ilevel].append(eigvals[ilevel])


for ilevel in range(2**2):
    plt.plot(slist, Englists[ilevel])

plt.xlabel("s")
plt.ylabel("Eigenenergy")
plt.minorticks_on()
plt.show()

## ↑ここまではエネルギー固有値の推移を見ただけ



## ↓ここから量子アニーリングを実行
_, psi0 = Hq.groundstate()

tau = 10. # annealing time
def fc(t, args):
    return t/tau

def fq(t, args):
    return 1 - t/tau

H = [[Hc, fc], [Hq, fq]] # total Hamiltonian

_, gs_Hc = Hc.groundstate()

# 0から1までを0.1づつ
tlist = np.linspace(0.0, tau, 101)
result = sesolve(H, psi0, tlist, [ket2dm(gs_Hc)])

plt.plot(result.times, result.expect[0])
plt.xlim(0.,10.)
plt.ylim(0.,1.)
plt.xlabel("t")
plt.ylabel("Probability of GS of Hc")
plt.minorticks_on()
plt.show()