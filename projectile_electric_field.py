# projectile_electric_field.py

import numpy as np
import matplotlib.pyplot as plt

# Coulomb constant (SI units)
K_COULOMB = 8.9875517923e9  # N·m^2 / C^2

def create_grid(xmin=-5, xmax=5, ymin=-5, ymax=5, n=200):
    """
    Create a 2D grid (X, Y) for plotting.
    - xmin, xmax, ymin, ymax: grid boundaries (float)
    - n: number of points per axis (int)
    Returns: X, Y (meshgrid)
    """
    x = np.linspace(xmin, xmax, n)
    y = np.linspace(ymin, ymax, n)
    X, Y = np.meshgrid(x, y)
    return X, Y

def compute_field(charges, X, Y, k=K_COULOMB, eps=1e-9):
    """
    Compute electric field components Ex and Ey at each grid point.
    
    charges: list of tuples [(q1, x1, y1), (q2, x2, y2), ...]
    X, Y: meshgrid arrays
    k: Coulomb constant
    eps: small value to avoid division by zero at charge locations
    Returns: Ex, Ey (electric field components at each grid point)
    """
    Ex = np.zeros_like(X, dtype=np.float64)
    Ey = np.zeros_like(Y, dtype=np.float64)

    for (q, x0, y0) in charges:
        Rx = X - x0          # x displacement from charge
        Ry = Y - y0          # y displacement from charge
        R2 = Rx**2 + Ry**2   # distance squared
        R = np.sqrt(R2) + eps
        R3 = R2 * R + eps    # r^3 with small eps to avoid division by zero

        Ex += k * q * Rx / R3  # x-component contribution (superposition)
        Ey += k * q * Ry / R3  # y-component contribution

    return Ex, Ey

def plot_field(X, Y, Ex, Ey, charges=None, figsize=(7,7),
               stream=True, density=1.5, cmap='inferno', scale=None):
    """
    Visualize the electric field.
    
    - X, Y: meshgrid
    - Ex, Ey: electric field components
    - charges: list of charges [(q, x, y), ...] to show (optional)
    - stream: True -> streamplot (flow lines), False -> quiver (arrows)
    - density: streamplot density
    - cmap: colormap for streamplot
    - scale: scale factor for quiver arrows (optional)
    """
    magnitude = np.sqrt(Ex**2 + Ey**2)
    color = np.log(magnitude + 1e-16)  # log scaling for better visualization

    plt.figure(figsize=figsize)
    if stream:
        plt.streamplot(X, Y, Ex, Ey, color=color, cmap=cmap, density=density, linewidth=1)
    else:
        skip = (slice(None, None, 6), slice(None, None, 6))  # subsample for clarity
        plt.quiver(X[skip], Y[skip], Ex[skip], Ey[skip], color='k', scale=scale)

    # Plot charges
    if charges is not None:
        for (q, x0, y0) in charges:
            if q > 0:
                plt.scatter(x0, y0, color='red', s=80 * np.log1p(abs(q)), marker='o', label=f'+{q} C')
            else:
                plt.scatter(x0, y0, color='blue', s=80 * np.log1p(abs(q)), marker='o', label=f'{q} C')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Electric Field')
    plt.axis('equal')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example 1: Single charge
    X, Y = create_grid(-5, 5, -5, 5, n=300)
    charges_single = [(1.0, 0.0, 0.0)]  # q = +1 C at origin
    Ex, Ey = compute_field(charges_single, X, Y)
    plot_field(X, Y, Ex, Ey, charges=charges_single, stream=True, density=1.5)

    # Example 2: Dipole (positive and negative charge)
    charges_dipole = [(1.0, -1.0, 0.0), (-1.0, 1.0, 0.0)]
    Ex2, Ey2 = compute_field(charges_dipole, X, Y)
    plot_field(X, Y, Ex2, Ey2, charges=charges_dipole, stream=True, density=2.0)

    # Example 3: Multiple charges
    charges_dipole2 = [(1, 1,0.0), (-1,-1,0.0), (1, 0, 1), (-1,0,-1)]
    Ex3, Ey3 = compute_field(charges_dipole2, X, Y)
    plot_field(X, Y, Ex3, Ey3, charges=charges_dipole2, stream=True, density=2.0)
