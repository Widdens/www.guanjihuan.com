import numpy as np
import matplotlib.pyplot as plt
from math import *   # 引入sqrt(), pi, exp等
import cmath  # 要处理复数情况，用到cmath.exp()
import functools  # 使用偏函数functools.partial()


def hamiltonian(k, N):  
    # 初始化为零矩阵
    h = np.zeros((4*N, 4*N))*(1+0j)   # 乘(1+0j)是为了把h0转为复数
    h11 = np.zeros((4*N, 4*N))*(1+0j)   # 元胞内
    h12 = np.zeros((4*N, 4*N))*(1+0j)   # 元胞间

    t=1
    a=1
    t0=0.2   # 层间跃迁
    V=0.2    # 层间的势能差为2V

    for i in range(N):
        h11[i*2+0, i*2+0] = V
        h11[i*2+1, i*2+1] = V


        h11[N*2+i*2+0, N*2+i*2+0] = -V
        h11[N*2+i*2+1, N*2+i*2+1] = -V


        h11[i*2+0, i*2+1] = -t 
        h11[i*2+1, i*2+0] = -t


        h11[N*2+i*2+0, N*2+i*2+1] = -t
        h11[N*2+i*2+1, N*2+i*2+0] = -t

        h11[i*2+0, N*2+i*2+1] = -t0
        h11[N*2+i*2+1, i*2+0] = -t0


    for i in range(N-1):
        h11[i*2+1, (i+1)*2+0] = -t 
        h11[(i+1)*2+0, i*2+1] = -t

        h11[N*2+i*2+1, N*2+(i+1)*2+0] = -t
        h11[N*2+(i+1)*2+0, N*2+i*2+1] = -t


    for i in range(N):
        h12[i*2+0, i*2+1] = -t
        h12[N*2+i*2+0, N*2+i*2+1] = -t

    h= h11 + h12*cmath.exp(-1j*k*a) + h12.transpose().conj()*cmath.exp(1j*k*a)    
    return h


def main():
    hamiltonian0 = functools.partial(hamiltonian, N=100)  # 使用偏函数，固定一些参数
    k = np.linspace(-pi, pi, 400)
    plot_bands_one_dimension(k, hamiltonian0)


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
        print(k0)
    for dim0 in range(dim):
        plt.plot(k, eigenvalue_k[:, dim0], '-k')  # -.
    # plt.savefig(filename + '.jpg')
    # plt.savefig(filename+'.eps')
    plt.show()


if __name__ == '__main__':  # 如果是当前文件直接运行，执行main()函数中的内容；如果是import当前文件，则不执行。
    main()
