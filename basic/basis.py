# 基礎知識

from qutip import *

# ケットベクトル
ket0 = Qobj([[1],[0]])
print(ket0)

# 基底 ∣0⟩,∣1⟩
basis_0 = basis(2,0)
basis_1 = basis(2,1)
print(basis_0)
print(basis_1)

# パウリ行列 σx,σy,σz
sigma_x = sigmax()
sigma_y = sigmay()
sigma_z = sigmaz()
print(sigma_x)
print(sigma_y)
print(sigma_z)