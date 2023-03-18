import numpy as np
from qutip import *
import matplotlib.pyplot as plt

nspins = 8 # 8スピン系
Jzz = {}
hz = {}

np.random.seed(seed=1234) # 乱数のシードを固定（同じ乱数が出力される）
for ispin in range(nspins-1):
    for jspin in range(ispin+1, nspins):
        Jzz[(ispin, jspin)] = np.random.randn()


for ispin in range(nspins):
    hz[ispin] = np.random.randn()

sz = [tensor([sigmaz() if i == j else qeye(2) for j in range(nspins)]) for i in range(nspins)]
sx = [tensor([sigmax() if i == j else qeye(2) for j in range(nspins)]) for i in range(nspins)]

# Hcの作成
Hc = 0.
for ispin in range(nspins-1):
    for jspin in range(ispin+1, nspins):
        Hc += -Jzz[(ispin, jspin)]*sz[ispin]*sz[jspin]

for ispin in range(nspins):
    Hc += -hz[ispin]*sz[ispin]


# Hqの作成
Hq = -sum(sx)

# 量子アニーリング途中過程での固有エネルギー
slist = np.linspace(0.0, 1.0, 101)
Englists = [[] for _ in range(12)] # エネルギー固有値を小さい順に12個計算する．

for s in slist:
    H = s*Hc + (1.-s)*Hq
    eigvals = H.eigenenergies()
    for ilevel in range(12):
        Englists[ilevel].append(eigvals[ilevel])

for ilevel in range(12):
    plt.plot(slist, Englists[ilevel])
    
plt.xlabel("s")
plt.ylabel("Eigenenergy")
plt.minorticks_on()
plt.show()


# 量子アニーリングを実行する
_, psi0 = Hq.groundstate()

tau = 10. # annealing time
def fc(t, args):
    return t/tau

def fq(t, args):
    return 1 - t/tau

H = [[Hc, fc], [Hq, fq]] # total Hamiltonian

_, gs_Hc = Hc.groundstate()

tlist = np.linspace(0.0, tau, 101)
result_sesolve = sesolve(H, psi0, tlist, [ket2dm(gs_Hc)])

plt.plot(result_sesolve.times, result_sesolve.expect[0])
plt.xlim(0.,10.)
plt.ylim(0.,1.)
plt.xlabel("t")
plt.ylabel("Probability of GS of Hc")
plt.minorticks_on()
plt.show()