# Validation of geolift.py

How to read this: in an A/A test (no true effect), a 90% interval should exclude zero in about 10% of runs. With a true effect, it should contain the true value in about 90% of runs. "Reported interval" is what the readout shows.

The parametric rows show why the script does not use the textbook interval alone: it ignores autocorrelation and excludes zero too often.

Simulated panels: Poisson counts around geo size times a shared factor (trend, weekly and yearly seasonality, AR(1) shocks) times geo-level AR(1) shocks. 200 panels per scenario, treated geos drawn at random. With 200 runs, a rate of 10% has a standard error of about 2 points.


200 simulated panels per scenario. Nominal interval: 90%. A well-calibrated method excludes zero in about 10% of A/A runs and covers the true lift in about 90% of runs.

| Scenario | Method | Excludes 0 | Covers truth | Mean lift | SD of lift |
|---|---|---:|---:|---:|---:|
| A/A, 40 geos, 20% treated, 28 days | TBR, reported interval | 6.0% | 94.0% | +0.43% | 2.10% |
| A/A, 40 geos, 20% treated, 28 days | SC, reported interval | 5.5% | 94.5% | +0.54% | 2.16% |
| A/A, 40 geos, 20% treated, 28 days | TBR, AR(1) parametric interval | 12.5% | 87.5% |  |  |
| A/A, 40 geos, 20% treated, 28 days | TBR, iid parametric interval | 14.5% | 85.5% |  |  |
| A/A, 15 geos, 20% treated, 28 days | TBR, reported interval | 8.0% | 92.0% | +0.27% | 2.63% |
| A/A, 15 geos, 20% treated, 28 days | SC, reported interval | 8.0% | 92.0% | +0.32% | 2.61% |
| A/A, 15 geos, 20% treated, 28 days | TBR, AR(1) parametric interval | 11.5% | 88.5% |  |  |
| A/A, 15 geos, 20% treated, 28 days | TBR, iid parametric interval | 16.5% | 83.5% |  |  |
| A/A, 40 geos, 120 days history | TBR, reported interval | 10.5% | 89.5% | +0.54% | 2.70% |
| A/A, 40 geos, 120 days history | SC, reported interval | 13.0% | 87.0% | +1.11% | 3.50% |
| A/A, 40 geos, 120 days history | TBR, AR(1) parametric interval | 16.5% | 83.5% |  |  |
| A/A, 40 geos, 120 days history | TBR, iid parametric interval | 18.5% | 81.5% |  |  |
| A/A, small volume (80/day total) | TBR, reported interval | 11.0% | 89.0% | +1.69% | 5.60% |
| A/A, small volume (80/day total) | SC, reported interval | 10.0% | 90.0% | +1.66% | 5.85% |
| A/A, small volume (80/day total) | TBR, AR(1) parametric interval | 13.5% | 86.5% |  |  |
| A/A, small volume (80/day total) | TBR, iid parametric interval | 15.0% | 85.0% |  |  |
| A/A, strong shared shocks | TBR, reported interval | 11.5% | 88.5% | +0.30% | 2.20% |
| A/A, strong shared shocks | SC, reported interval | 11.0% | 89.0% | +0.37% | 2.31% |
| A/A, strong shared shocks | TBR, AR(1) parametric interval | 15.5% | 84.5% |  |  |
| A/A, strong shared shocks | TBR, iid parametric interval | 20.5% | 79.5% |  |  |
| Go-dark -10%, 40 geos | TBR, reported interval | 99.0% | 89.0% | -9.64% | 2.13% |
| Go-dark -10%, 40 geos | SC, reported interval | 97.0% | 91.0% | -9.55% | 2.19% |
| Go-dark -10%, 40 geos | TBR, AR(1) parametric interval | 99.5% | 87.0% |  |  |
| Go-dark -10%, 40 geos | TBR, iid parametric interval | 99.5% | 84.0% |  |  |
| Go-dark -25%, 15 geos | TBR, reported interval | 100.0% | 89.5% | -24.55% | 2.05% |
| Go-dark -25%, 15 geos | SC, reported interval | 100.0% | 89.0% | -24.51% | 2.08% |
| Go-dark -25%, 15 geos | TBR, AR(1) parametric interval | 100.0% | 94.0% |  |  |
| Go-dark -25%, 15 geos | TBR, iid parametric interval | 100.0% | 91.5% |  |  |
| Heavy-up +8%, 40 geos | TBR, reported interval | 98.5% | 93.5% | +8.41% | 1.97% |
| Heavy-up +8%, 40 geos | SC, reported interval | 99.0% | 95.0% | +8.49% | 2.06% |
| Heavy-up +8%, 40 geos | TBR, AR(1) parametric interval | 99.5% | 83.0% |  |  |
| Heavy-up +8%, 40 geos | TBR, iid parametric interval | 100.0% | 80.5% |  |  |

## Design MDE check

Design run on 365 days of pre-period, then the validation MDE is injected as a go-dark effect in the chosen group. Nominal power is 80%.

- Simulations: 200
- Median predicted MDE: 5.03%
- Share detected at the predicted MDE: 78.5%
