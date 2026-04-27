# -Linear-Transformation-Fractal-Generator
This project explores how repeated linear transformations generate fractal-like geometric patterns. Using NumPy and Matplotlib, it applies affine transformations iteratively to visualize growth, analyze parameter variations, and study eigenvalues of transformation matrices. The project highlights the connection between linear algebra concepts and emergent visual structures.
## Features

- Generates a fractal-like curve using affine transformation
- Shows growth across different iteration counts
- Compares original and modified transformation parameters
- Computes eigenvalues and eigenvectors of the transformation matrix
- Saves generated plots inside the `results/` folder

## Technologies Used

- Python
- NumPy
- Matplotlib

## Mathematical Idea

The project uses the iterative transformation:

```text
x(n+1) = A x(n) + b
