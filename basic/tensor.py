# 多スピン系用に、テンソル積も使える

from qutip import *

# 2スピンの系で ∣01⟩
tensor_0 = tensor(basis(2, 0), basis(2, 1))
print(tensor_0)

# テンソル積 σz⊗σz
tensor_1 = tensor(sigmaz(), sigmaz())
print(tensor_1)
