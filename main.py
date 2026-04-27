import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)

A_ORIGINAL = np.array([[0.85, 0.04],
                       [-0.04, 0.85]])

A_MODIFIED = np.array([[0.9, 0.1],
                       [-0.1, 0.9]])

b = np.array([0, 1.6])
N = 10000


def generate_points(A, iterations=N):
    x = np.array([0, 0])
    points = []

    for _ in range(iterations):
        x = A @ x + b
        points.append(x)

    return np.array(points)


def plot_main_fractal():
    points = generate_points(A_ORIGINAL)

    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], s=0.5)
    plt.title("Generated Fractal")
    plt.savefig("results/fractal_main.png")
    plt.show()


def plot_iterations():
    points = generate_points(A_ORIGINAL)
    snapshots = [10, 100, 1000]

    for n in snapshots:
        plt.figure()
        plt.scatter(points[:n, 0], points[:n, 1], s=1)
        plt.title(f"Iteration {n}")
        plt.savefig(f"results/iter_{n}.png")
        plt.show()


def compare_parameters():
    points1 = generate_points(A_ORIGINAL)
    points2 = generate_points(A_MODIFIED)

    plt.scatter(points1[:, 0], points1[:, 1], s=0.5, label="Original")
    plt.scatter(points2[:, 0], points2[:, 1], s=0.5, label="Modified")
    plt.legend()
    plt.title("Parameter Comparison")
    plt.savefig("results/comparison.png")
    plt.show()


def compute_eigen_values():
    eigvals, eigvecs = np.linalg.eig(A_ORIGINAL)

    print("Eigenvalues:")
    print(eigvals)

    print("\nEigenvectors:")
    print(eigvecs)


def main():
    parser = argparse.ArgumentParser(description= "Fractal Generator CLI")
    parser.add_argument(
        "mode",
        choices=["fractal", "iter","compare","eigen"],
        help = "Select what to run"
    )
    args = parser.parse_args()
    if args.mode == "fractal":
        plot_main_fractal()
    elif args.mode == "iter":
        plot_iterations()
    elif args.mode == "compare":
        compare_parameters()
    elif args.mode == "eigen":
        compute_eigen_values()


if __name__ == "__main__":
    main() 