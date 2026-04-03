# MNA Calc

A numerical analysis calculator I built for my engineering courses — designed to run both on PC and on Casio calculators (Python-compatible models).

## What it does

### Numerical Integration
Five methods, from basic to advanced:
- **Riemann Sums** — left or right endpoint approximations
- **Trapezoidal Method** — linear interpolation between points
- **Midpoint Method** — centered rectangles
- **Simpson's Method** — parabolic interpolation
- **Romberg Method** — Richardson extrapolation, for when you need precision

### Root-Finding
- **Fixed Point** — classic iterative method
- **Newton-Raphson** — quadratic convergence
- **Chord Method** — secant-like approximation

## Getting started

Just Python 3.x, no external dependencies.
```bash
git clone https://github.com/Ant3ch/MNA-Calc.git
cd MNA-Calc
python main.py
```

## How to use it

Fully text-menu driven, keyboard-navigable:

1. From the **main menu**, pick a module:
   - Numerical Integration
   - Fixed Point & Root-Finding
   - Explanations (detailed algorithm descriptions)
   - Credits

2. **Enter functions** using standard Python syntax:
   - e.g. `x**2 + 3*x - 1` for $x^2 + 3x - 1$
   - Supported: `sin()`, `cos()`, `sqrt()`, `exp()`, `log()`, etc.

3. **Navigation**: `B` to go back, `P` / `N` to paginate

## Expected inputs

**Integration**: a function, an interval $[a, b]$, a number of subdivisions $n$

**Root-finding**: a function (or iteration function), a starting point $x_0$, a tolerance, and a max iteration count

## Quick example
```python
# Computing the integral of x² over [0, 1] using Simpson's method
# 1. Select "Numerical Integration"
# 2. Choose "Simpson's Method"
# 3. Function: x**2
# 4. Bounds: a=0, b=1
# 5. Subdivisions: n=100
# → Result displayed immediately
```

## Project structure
MNA Calc/
├── main.py                 # Entry point
├── menu_core.py            # Menu management
├── menu_principal.py       # Main menu
├── menu_integration.py     # Integration methods
├── menu_point_fixe.py      # Root-finding methods
├── menu_explications.py    # Algorithm explanations
├── credit.py               # Credits
├── utils.py                # Utility functions
└── LICENSE

## Compatibility

Works on Windows, macOS, and Linux. Also compatible with Casio Python-enabled calculators — which is honestly the main reason the interface is menu-based.

## Contributing

Issues, suggestions, and pull requests are welcome.

---

*MNA Calc — numerical analysis, anywhere*