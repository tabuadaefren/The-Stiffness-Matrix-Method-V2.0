import numpy as np 
import matplotlib.pyplot as plt

def beamPlot(beamLength, loadPositions, loadForces, beamSupport):

    l=beamLength      #Scalar
    a=loadPositions   #Vector
    W=loadForces      #Vector
    x=np.array(range(0,l))

    E=200*10**9      #Constant [N/m^2]
    I=0.001          #Constant [m^4]


#Makes an empty vector with the same size as x
    y=np.empty_like(x, dtype=float)

    for i in range(np.size(x)):  #Continues as long as the vector x
        for v in range(np.size(a)):

            if a[v]==[ ] and W[v]==[ ]:
                return np.zeros(np.size(x))

            elif beamSupport=="both" and x[i]<a[v]:
                 y[i]=np.sum(((W[v]*(l-a[v])*x[i])/(6*E*I*l))*(l**2-x[i]**2-(l-a[v])**2))
            elif beamSupport=="both" and x[i]>=a[v]:   
                 y[i]=np.sum(W[v]*a[v]*(l-x[i])/(6*E*I*l)*(l**2-(l-x[i])**2-a[v]**2))                         
            elif beamSupport=="cantilever" and x[i]<a[v]:
                 y[i]=np.sum((W[v]*x[i]**2)/(6*E*I)*(3*a[v]-x[i]))
            elif beamSupport=="cantilever" and x[i]>=a[v]:
                 y[i]=np.sum((W[v]*a[v]**2)/(6*E*I)*(3*x[i]-a[v]))

        deflection=y 


    plt.xlim([0,l])
    plt.title("Beam deflection")
    plt.plot(x, deflection)
plt.show()