
import numpy as np

# %% ------------------Exercise 1----------------------------------
"""In this problem, we will investigate the perceptron algorithm with different iteration ordering.
    Consider applying the perceptron algorithm through the origin based on a small training set 
    containing three points:
    x(1)=[-1,-1], 	y(1)=1
    x(2)=[1,0],  y(2)=-1 
    x(3)=[-1, 1.5], y(3)=1
    Given that the algorithm starts with theta=0, 
    the first point that the algorithm sees is always considered a mistake. 
    The algorithm starts with some data point and then cycles through the data (in order)
    until it makes no further mistakes. 
"""
## How many mistakes does the algorithm make until convergence
#  if the algorithm starts with data point ? 
# How many mistakes does the algorithm make if it starts with data point ? 


# Lets make a list of the vectors
x=np.array([[-1,-1],[1,0],[-1,10]])
y=np.array([1,-1,1])

# perceptron algorithm

T=100
theta=np.array([0,0])
theta_progress=np.array([])
for t in range(T): 
    for i in np.array([1,2,0]):
        if (y[i]*(np.dot(theta,x[i])))<=0:
            theta=theta+(y[i]*x[i])
            # theta_progress=np.concatenate((theta_progress,theta),axis=1)
            print(theta)



#----------------- Percetron with offset ----------------------------------------------------
# %%
#  ------------------Exercise 2a----------------------------------

x=np.array([[-4,2],[-2,1],[-1,-1],[2,2],[1,-2]])
y=np.array([1,1,-1,-1,-1])

T=2
theta=np.array([0,0])
theta_0=0;
for t in range(T): 
    for i in np.arange(len(x)):
        print(x[i])
        if (y[i]*(np.dot(theta,x[i])))<=0:
            theta=theta+(y[i]*x[i])
            theta_0=theta_0+y[i]
            print("theta value is {}".format(theta))
            print("theta 0 value is {}".format(theta_0))
            print("n iteration value is  {}".format(i+1))

print("Final theta value is {}".format(theta))
print("Final theta 0 value is {}".format(theta_0))


# %% ------------------Exercise 2b----------------------------------
"""Provide one example of a different initialization "theta"
 of such that the perceptron algorithm with this initialization
  would not produce any mistakes during a run through the data. 
"""
x=np.array([[-4,2],[-2,1],[-1,-1],[2,2],[1,-2]])
y=np.array([1,1,-1,-1,-1])

T=100000
theta=np.array([0,0])
theta_0=0;
convergence=0;
while convergence!=5:
    print(convergence)
    if convergence==5:
        print("Final theta value is {}".format(theta))
        print("Final theta 0 value is {}".format(theta_0))
        break
    for i in np.arange(len(x)):
        if (y[i]*(np.dot(theta,x[i])))<=0:
            theta=theta+(y[i]*x[i])
            theta_0=theta_0+y[i]
            
            # print("theta value is {}".format(theta))
            # print("theta 0 value is {}".format(theta_0))
            # print("n iteration value is  {}".format(i+1))
            convergence=0

        else:
            convergence+=1
            # print (convergence)
print("Final theta value is {}".format(theta))
print("Final theta 0 value is {}".format(theta_0))


# %%
