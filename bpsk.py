import numpy as np
import matplotlib.pyplot as plt

def func_sin(bit, density):
    if bit == "0":
        return [-np.sin(i)+np.random.rand()*0.5 for i in np.linspace(0, 4*np.pi, num=density)]
    if bit == "1":
        return [np.sin(i)+np.random.rand()*0.5 for i in np.linspace(0, 4*np.pi, num=density)]


def func_lines(bit, density):
    if bit == "0":
        return [0 for i in np.linspace(0, 4*np.pi, num=density)]
    if bit == "1":
        return [1 for i in np.linspace(0, 4*np.pi, num=density)]

def func_blabla(bit, density):
    if bit == "0":
        return [-np.sin(i) for i in np.linspace(0, 4*np.pi, num=density)]
    if bit == "1":
        return [np.sin(i) for i in np.linspace(0, 4*np.pi, num=density)]

def noise(bit, density): 
    return [np.random.rand() for i in np.linspace(0, 4*np.pi, num=density)]

def bit2figdata_generalized(bit_string, func, density=2000):
    n = len(bit_string) 
    xdata = np.linspace(0, n*2*np.pi, num=density*n)
    ydata = np.array([])
    for bit in bit_string:
        y = func(bit, density)
        ydata = np.concatenate((ydata, y))
    return xdata, ydata

# Functional Method
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.3])
ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.3])

# x, y = bit2figdata("100101")
# x2, y2 = bit2figdata2("100101")
x, y = bit2figdata_generalized("100101", func_blabla)
x2, y2 = bit2figdata_generalized("100101", func_sin)

# ax.plot(x, y, color="black")
# ax2.plot(x2, y2, color="black")

# plt.show()

sp = np.fft.fft(y2)
freq = np.fft.fftfreq(y2.shape[-1])
ax.plot(freq, sp.real, freq, sp.imag)

sp = np.fft.fft(y)
freq = np.fft.fftfreq(y.shape[-1])
ax2.plot(freq, sp.real, freq, sp.imag)
plt.show()