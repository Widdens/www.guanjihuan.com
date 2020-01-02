import numpy as np
import matplotlib.pyplot as plt
from math import *   # 引入sqrt(), pi, exp等
import cmath  # 要处理复数情况，用到cmath.exp()
import functools  # 使用偏函数functools.partial()


def hamiltonian(k, N, t):  # 准一维方格子哈密顿量
    # 初始化为零矩阵
    h00 = np.zeros((N, N))*(1+0j)   # 乘(1+0j)是为了把h0转为复数
    h01 = np.zeros((N, N))*(1+0j)
    for i in range(N-1):   # 原胞内的跃迁h00
        h00[i, i+1] = t
        h00[i+1, i] = t
    for i in range(N):   # 原胞间的跃迁h01
        h01[i, i] = t
    matrix = h00 + h01*cmath.exp(-1j*k) + h01.transpose().conj()*cmath.exp(1j*k)
    return matrix


def main():
    H_k = functools.partial(hamiltonian, N=10, t=1)  # 使用偏函数，固定一些参数
    k = np.linspace(-pi, pi, 300)
    plot_bands_one_dimension(k, H_k)


def plot_bands_one_dimension(k, hamiltonian, filename='bands_1D'):
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
        plt.plot(k, eigenvalue_k[:, dim0], '-k')  # -.
    # plt.savefig(filename + '.jpg')
    # plt.savefig(filename+'.eps')
    plt.show()


if __name__ == '__main__':  # 如果是当前文件直接运行，执行main()函数中的内容；如果是import当前文件，则不执行。
    main()
