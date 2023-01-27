# 量子アニーリングにおける応用 エネルギースペクトルの計算

import numpy as np
from qutip import *
import matplotlib.pyplot as plt
import random

N = 4 # 4スピン系
J = {} # 相互作用係数J_ij
h = {} # 縦磁場h_i

for i in range(N-1):
    for j in range(i+1, N):
        J[(i,j)] = random.gauss(0,1)

for i in range(N):
    h[i] = random.gauss(0,1)

# スピン演算子の作成
sz = []
for i in range(N):
    tensor_list = []
    for j in range(N):
        if i == j:
            tensor_list.append(sigmaz())
        else :
            tensor_list.append(qeye(2))
    
    sz.append(tensor(tensor_list))

# スピン演算子の作成
sx = []
for i in range(N):
    tensor_list = []
    for j in range(N):
        if i == j:
            tensor_list.append(sigmax())
        else :
            tensor_list.append(qeye(2))
        
    sx.append(tensor(tensor_list))

# ハミルトニアンH_0の作成
H0 = 0
for i in range(N-1):
    for j in range(i+1, N):
        H0 += -J[(i,j)] * sz[i] * sz[j]

for i in range(N):
    #print(h[i]*sz[i])
    H0 += -h[i] * sz[i]

H1 = -sum(sx)

# エネルギースペクトルの計算（パラメタsを0から1まで動かした時に、固有エネルギーがどう変化するか）
slist = np.linspace(0.0, 1.0, 101)
Elists = [[] for i in range(2**N)]

for s in slist:
    H = s * H0 + (1-s) * H1
    evals = H.eigenenergies() # 固有エネルギー（固有値）を返す

    for i in range(2**N):
        Elists[i].append(evals[i])

for i in range(2**N):
    plt.plot(slist, Elists[i])

plt.show()
