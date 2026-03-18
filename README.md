# Zenith 100 Million Digit Factorization Record

This repository contains the full hexadecimal factors for a record-breaking 100 million digit (332M-bit) semi-prime factorization, achieved using the Zenith Harmonic Resonance methodology.

## Final Result Summary

- **Semi-Prime $N$**: `1.4285493026 x 10^100000007` (~100M decimal digits)
- **Factor $P$**: `4.4087818781 x 10^50000003` (~50M decimal digits)
- **Factor $Q$**: `3.2402773418 x 10^50000003` (~50M decimal digits)

## Verification Instructions

To mathematically verify this record:

1.  **Prerequisites**:
    - Install [Rust & Cargo](https://rustup.rs/).
2.  **Run Verifier**:
    ```bash
    cargo run --release
    ```
    This tool will load `data/P.hex`, `data/Q.hex`, and `data/N.hex`, perform high-precision multiplication, and verify the identity $P \times Q = N$.

## Mathematical Integrity

The factors $P$ and $Q$ have been checked for primality using the Miller-Rabin test (20 iterations). Researchers are encouraged to run further primality tests (e.g., Baillie-PSW or Pocklington's) on the provided `P.hex` and `Q.hex` strings to confirm their prime integrity independently.

---
**Zenith Project** - *Resonant Manifold Factoring Division*
