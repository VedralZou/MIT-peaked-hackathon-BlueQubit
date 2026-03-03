import time
import warnings
import os

os.environ["BLUEQUBIT_DEQART_INTERNAL_DISABLE_STRICT_VALIDATIONS"] = "1"
warnings.filterwarnings("ignore", category=UserWarning)

import numpy as np
import requests
from qiskit import QuantumCircuit

import bluequbit
bq = bluequbit.init()

# --------------------------
# Get Circuit (tutorial style: load from raw URL)
# --------------------------
url = "https://raw.githubusercontent.com/BlueQubitDev/sdk-examples/main/peaked_circuits/qasm/P4_gentle_mound.qasm"
qasm = requests.get(url).text
qc = QuantumCircuit.from_qasm_str(qasm)

# Remove measurements for expectation-value evaluation (same idea as tutorial)
qc.remove_final_measurements(inplace=True)

print("Qubits:", qc.num_qubits)
print("Gate counts:", qc.count_ops())

# --------------------------
# Marginal Attack: infer each bit from sign of <Z_i>
# --------------------------
n = qc.num_qubits

# Build single-qubit Z observables (Pauli strings)
Z_ops = []
for i in range(n):
    pauli_str = "".join("Z" if j == i else "I" for j in range(n))
    pauli_str = pauli_str[::-1]  # Qiskit little-endian convention (as in tutorial)
    Z_ops.append([(pauli_str, 1.0)])

z_expvals = []
t0 = time.time()

for i, Z_op in enumerate(Z_ops):
    result = bq.run(
        qc,
        device="pauli-path",
        pauli_sum=Z_op,
        expectation_value=True,
    )
    z_expvals.append(result.expectation_value)
    print(f"qubit {i}: <Z_{i}> = {result.expectation_value:.6f}")

dt = time.time() - t0
z_expvals = np.array(z_expvals)

# If <Z_i> > 0 => bit 0 favored; if <Z_i> < 0 => bit 1 favored
bits = (z_expvals < 0).astype(int)
peak_bitstring = "".join(str(b) for b in bits)

print(f"\nTotal time: {dt:.2f} s")
print("Peak bitstring inferred from marginals:", peak_bitstring)
