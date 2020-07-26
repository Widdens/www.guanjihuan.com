import numpy as np
import matplotlib.pyplot as plt
from math import *   # 引入sqrt(), pi, exp等
import cmath  # 要处理复数情况，用到cmath.exp()


def hamiltonian(k):  # SSH模型
    v=0.6
    w=1
    matrix = np.zeros((2, 2))*(1+0j)   # 乘(1+0j)是为了把h0转为复数
    matrix[0,1] = v+w*cmath.exp(-1j*k)
    matrix[1,0] = v+w*cmath.exp(1j*k)
    return matrix


def main():
    k = np.linspace(-pi, pi, 100)
    plot_bands_one_dimension(k, hamiltonian)


def plot_bands_one_dimension(k, hamiltonian):
    dim = hamiltonian(0).shape[0]
    dim_k = k.shape[0]
    eigenvalue_k = np.zeros((dim_k, dim))  # np.zeros()里要用tuple
    i0 = 0
    for k0 in k:
        matrix0 = hamiltonian(k0)
        eigenvalue, eigenvector = np.linalg.eig(matrix0)
        eigenvalue_k[i0, :] = np.sort(np.real(eigenvalue[:]))
        i0 += 1
    for dim0 in range(dim):
        plt.plot(k, eigenvalue_k[:, dim0], '-k')
    plt.show()


if __name__ == '__main__':  # 如果是当前文件直接运行，执行main()函数中的内容；如果是import当前文件，则不执行。
    main()
