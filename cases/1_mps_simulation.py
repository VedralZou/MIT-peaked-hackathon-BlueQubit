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

# Get Circuits (local file from your repo)
qc = QuantumCircuit.from_qasm_file("circuits/P1_little_peak.qasm")

print("Qubits:", qc.num_qubits)
print("Gate counts:", qc.count_ops())

# MPS simulation
shots = 500
bond_dim = 32

t0 = time.time()
results_mps = bq.run(
    qc,
    device="mps.cpu",
    shots=shots,
    options={"mps_bond_dimension": bond_dim},
)
dt = time.time() - t0

counts = results_mps.get_counts()
top10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(f"\nMPS runtime: {dt:.2f} s")
print("Top-10 most frequent bitstrings (MPS):")
for b, c in top10:
    print(f"{b}: {c}")

print("\nPeak bitstring (MPS):", top10[0][0])
