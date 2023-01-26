# ハミルトニアン

from qutip import *

H = sigmax()
energy = H.eigenenergies() #固有エネルギー（固有値）を返す
print(energy)

evals, ekets = H.eigenstates() # 固有エネルギーと固有状態を返す
print(evals)
print(ekets)

evals_0, ekets_0 = H.groundstate() # 基底状態の固有エネルギーと固有状態を返す
print(evals_0)
print(ekets_0)