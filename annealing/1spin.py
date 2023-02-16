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

# 0から1までを0.01づつ
slist = np.linspace(0.0, 1.0, 101)
Englists = [[] for _ in range(2)]

for s in slist:
    H = s*Hc + (1.-s)*Hq #ハミルトニアン生成
    eigvals = H.eigenenergies() # エネルギー固有値

    for i in range(2):
        Englists[i].append(eigvals[i])

for i in range(2):
    plt.plot(slist, Englists[i]) # x軸はslist(0から1), y軸はエネルギー固有値（2種類）
    
plt.xlabel("s")
plt.ylabel("Eigenenergy")
plt.minorticks_on()
plt.show()

