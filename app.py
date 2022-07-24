import numpy                as     np
import matplotlib.pyplot    as     plt
from   matplotlib.animation import FuncAnimation
np.set_printoptions(precision=3, suppress=False)
from signals import signalSine, signalSquare, signalTriangle

fs = 1000
N = 1000
fase = 0
amp = 1             
f01 = 0.1 * fs
f02 = 1.1 * fs
f03 = 0.49 * fs
f04 = 0.51 * fs

m1 = signalSine(fs,f01, amp, N, fase)
m2 = signalSquare(fs,f01, amp, N)
m3 = signalTriangle(fs,f01, amp, N)

plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal sine')
plt.plot(m1[1],m1[0],'ro-')
plt.show()

plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal Square')
plt.plot(m2[1],m2[0],'ro-')
plt.show()

plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal Triangle')
plt.plot(m3[1],m3[0],'ro-')
plt.show()

m4 = signalSine(fs,f02, amp, N, fase)
plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal sine, ejercicio 3.2.1')
plt.plot(m1[1],m1[0],'ro-')
plt.plot(m4[1],m4[0],'ro-')
plt.show()

m5 = signalSine(fs,f03, amp, N, fase)
m6 = signalSine(fs,f04, amp, N, fase)
plt.xlabel('Time') 
plt.ylabel('Amplitude') 
plt.title('Signal sine, ejercicio 3.2.2')
plt.plot(m5[1],m5[0],'ro-')
plt.plot(m6[1],m6[0],'bo-')
plt.show()
