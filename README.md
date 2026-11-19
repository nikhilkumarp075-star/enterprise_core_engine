# Lean 4 Formalization Practice

Original educational examples for exploring theorem proving in Lean 4.

## Contents
- `Algebra.lean`: basic natural-number equalities
- `Logic.lean`: conjunction, disjunction, implication, contradiction
- `NumberTheory.lean`: inequalities, parity, divisibility

## Requirements
Install Lean 4 and Mathlib. These examples have **not been compiled in this environment**; they are draft examples to verify locally before describing them as machine-checked proofs.

To verify with a Mathlib project, place the files inside the project and run:

```bash
lake env lean Algebra.lean
lake env lean Logic.lean
lake env lean NumberTheory.lean
```

The project is a learning portfolio, not evidence of prior professional Lean experience. Please accurately represent your own contributions and experience when applying for work.
