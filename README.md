# Nikhil | Mathematics, Python & Formal Methods Portfolio

A reproducible starter portfolio demonstrating numerical data generation, mathematical algorithms, unit tests, and introductory Lean 4 theorem statements/proofs.

## Included
- `src/run_analysis.py`: creates 10,000 **synthetic** observations with a fixed seed and writes summary statistics to `RESULTS.md`.
- `src/number_theory.py`: prime testing, Euclidean GCD, and Fibonacci sequence.
- `tests/test_number_theory.py`: Python unit tests.
- `lean/BasicProofs.lean`: three beginner Lean 4 examples, **not compiled or verified in this environment**.

## Reproduce
```bash
python -m unittest discover -s tests -v
python src/run_analysis.py
```

## Verify Lean examples
Install Lean 4 with elan, then run:
```bash
lake env lean lean/BasicProofs.lean
```

## Integrity note
This repository is a newly created portfolio starter, not evidence of prior professional experience, published research, or contributions to mathlib. Describe Lean experience in applications based only on what you have personally completed and verified.
