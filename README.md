# -Linear-Transformation-Fractal-Generator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Made With](https://img.shields.io/badge/Made%20with-NumPy%20%26%20Matplotlib-orange)


This project explores how repeated linear transformations generate fractal-like geometric patterns. Using NumPy and Matplotlib, it applies affine transformations iteratively to visualize growth, analyze parameter variations, and study eigenvalues of transformation matrices. The project highlights the connection between linear algebra concepts and emergent visual structures.
## Features

- Generates a fractal-like curve using affine transformation
- Shows growth across different iteration counts
- Compares original and modified transformation parameters
- Computes eigenvalues and eigenvectors of the transformation matrix
- Saves generated plots inside the `results/` folder
-Modular CLI-based execution
- Animated fractal generation using Matplotlib

## Technologies Used

- Python
- NumPy
- Matplotlib

## Mathematical Idea

The project uses the iterative transformation:

```text
x(n+1) = A x(n) + b

Where:
- **A** -> transform matrix
- **b** -> translation vector

Repeated application produces comple geometric patterns.

## Key Concepts Demonstrated
- Linear transformations
- Eigenvalues and system stability
- Iterative systems and convergence
- Parameters sensitivity analysis

## Future Improvements
- Support custom matrices via CLI
- Optimize performance for large iterations
- Convert into interactive web app
