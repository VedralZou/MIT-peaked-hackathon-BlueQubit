## Structural Perspective on Classical Attacks

Peaked circuits are often described as “random-looking but structured.”  
What the three classical strategies reveal is not just how to recover the peak bitstring, but **where classical power actually comes from**.

### MPS Simulation — Compression as a Proxy for Structure

The MPS approach does not try to understand the circuit.  
It simply asks:

> Can the quantum state be compressed?

If entanglement is sufficiently localized, the state admits a low bond-dimension representation.  
In that regime, classical simulation succeeds because the quantum state does not fully explore Hilbert space.

This is a *structural statement* about entanglement:

- If the circuit distributes entanglement globally → compression fails.
- If correlations remain limited → sampling recovers the peak.

MPS does not exploit peakedness directly.  
It exploits *limited entanglement*.

---

### Marginal Attack — Bias as Information Leakage

The marginal attack changes perspective.

Instead of approximating the full state, it asks:

> Does each qubit individually “know” the peak?

If the output distribution concentrates sharply around a dominant bitstring, then each qubit exhibits a strong local bias:

\[
\langle Z_i \rangle \neq 0
\]

This means that global structure leaks into single-qubit marginals.

The success of this attack implies something subtle:

Peaked circuits encode global information in locally accessible observables.

That is not a generic property of random circuits.

This method does not simulate the state.  
It extracts information from expectation structure.

---

### Pauli-Path Simulation — Operator-Level Exploitation

The Pauli-path simulator goes one layer deeper.

Instead of compressing the state (MPS)  
or sampling observables naively (marginal attack),  
it leverages the algebraic structure of the circuit.

In the Heisenberg picture, observables propagate backward.  
Low-weight Pauli terms dominate when the circuit structure permits it.

If those paths remain controlled under truncation, expectation values can be computed efficiently.

This is no longer state-based simulation.  
It is structure-aware operator evolution.

The computational gain comes from:

- Gate locality
- Controlled Pauli growth
- Truncatable operator spreading

This is fundamentally different from brute-force classical simulation.

---

## What the Three Cases Suggest

Across the three methods, a pattern emerges:

| Method | What it Exploits |
|--------|------------------|
| MPS | Limited entanglement |
| Marginal Attack | Local bias induced by peakedness |
| Pauli-Path | Controlled operator growth |

The difficulty of peaked circuits is therefore not purely about circuit size.  
It depends on how these structural properties scale:

- Entanglement growth
- Marginal concentration
- Operator spreading complexity

In other words, classical hardness is not binary.  
It is structural.
