import numpy as np
from qutip import *
import matplotlib.pyplot as plt
import random

Jzz = {(0,1): 0.8} # 相互作用
hz = {0: 0.2, 1:1.2} # 局所磁場

#スピン演算子の準備
sz = [tensor([sigmaz() if i == j else qeye(2) for j in range(2)]) for i in range(2)]
sx = [tensor([sigmax() if i == j else qeye(2) for j in range(2)]) for i in range(2)]