import numpy as np
import matplotlib.pyplot as plt



# insert dri ang beam parameters or iimport
#length, height, width, point where load begins, gravity, rho, E, I, w

l=200		     #mm, lenght
h=100                #mm, height
b=10  		     #mm, width
a=0                  #mm, point where load begins
g=9810               #mm/s^2
rho=7.850*(10**-9)   #g/mm^3
E = 210*(10**3)      #N/mm^2
I = (b*h**3)/12      #Second moment of area for square cross section
w=rho*g*b*h    

#reaction at the support, moment on the support

r1=w*(l-a)           #Reaction at the support
m1=(w/2)*(l**2-a**2) #Moment on the support



#formula
x=np.linspace(0,l)
y = (1/float (E*I))*(-(m1/2)*x**2+(r1/6)*x**3-(w/24)*(x>=a)*x**4)


maxy=min(y) #max values

textstr3 = 'max=%.5f (mm)'%(maxy) #diagram plot
props = dict(boxstyle='round', facecolor='white')


deflection = y

plt.plot(x, deflection)

plt.show()
