import numpy as np
from math import *
import matplotlib.pyplot as plt


def main():
    n =  0.5
    k1 = np.arange(-n*pi, n*pi, n/20)
    k2 = np.arange(-n*pi, n*pi, n/20)
    plot_bands_two_dimension(k1, k2, hamiltonian)


def hamiltonian(kx,kz,ky=0):  # Weyl semimetal
    A = 1
    M0 = 1
    M1 = 1
    H = A*(kx*sigma_x()+ky*sigma_y())+(M0-M1*(kx**2+ky**2+kz**2))*sigma_z()
    return H


def sigma_x():
    return np.array([[0, 1],[1, 0]])


def sigma_y():
    return np.array([[0, -1j],[1j, 0]])


def sigma_z():
    return np.array([[1, 0],[0, -1]])


def plot_bands_two_dimension(k1, k2, hamiltonian):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter
    dim = hamiltonian(0, 0).shape[0]
    dim1 = k1.shape[0]
    dim2 = k2.shape[0]
    eigenvalue_k = np.zeros((dim2, dim1, dim))
    i0 = 0
    for k10 in k1:
        j0 = 0
        for k20 in k2:
            matrix0 = hamiltonian(k10, k20)
            eigenvalue, eigenvector = np.linalg.eig(matrix0)
            eigenvalue_k[j0, i0, :] = np.sort(np.real(eigenvalue[:]))
            j0 += 1
        i0 += 1
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    k1, k2 = np.meshgrid(k1, k2)
    for dim0 in range(dim):
        ax.plot_surface(k1, k2, eigenvalue_k[:, :, dim0], cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.xlabel('kx')
    plt.ylabel('kz') 
    ax.set_zlabel('E')  
    plt.show()


if __name__ == '__main__':
    main()