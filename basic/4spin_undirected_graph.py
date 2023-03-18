from qutip import *

# 単位行列
print(qeye(2))

# σ_z
print(sigmaz())

# σ_1z(σz⊗I⊗I⊗I)
tensor1 = tensor(sigmaz(), qeye(2), qeye(2), qeye(2))
print(tensor1)

# σ_2z(I⊗σz⊗I⊗I)
tensor2 = tensor(qeye(2), sigmaz(), qeye(2), qeye(2))
print(tensor2)

# σ_3z(I⊗I⊗σz⊗I)
tensor3 = tensor(qeye(2), qeye(2),sigmaz(), qeye(2))
print(tensor3)

# σ_4z(I⊗I⊗I⊗σz)
tensor4 = tensor(qeye(2), qeye(2), qeye(2),sigmaz())
print(tensor4)

print(tensor1 * tensor2)
print(tensor1 * tensor4)
print(tensor2 * tensor4)
print(tensor3 * tensor4)
