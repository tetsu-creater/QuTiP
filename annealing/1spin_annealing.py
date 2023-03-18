import numpy as np
from qutip import *
import matplotlib.pyplot as plt
import random

# 縦磁場h_0の設定
hz = {}
hz[0] = 1.2

# H_c を作成
Hc = -hz[0] * sigmaz()

# H_q を作成
Hq = - sigmax()

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
result_sesolve = sesolve(H, psi0, tlist, [ket2dm(gs_Hc)])

plt.plot(result_sesolve.times, result_sesolve.expect[0])
plt.xlim(0.,10.)
plt.ylim(0.,1.)
plt.xlabel("t")
plt.ylabel("Probability of GS of Hc")
plt.minorticks_on()
plt.show()
