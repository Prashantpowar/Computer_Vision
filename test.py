import numpy as np



a = np.array((1,1,1))

b = np.array((10,10,10))

c = np.array((1,5,5))

# if np.greater_equal(a,c) and np.less_equal(b,c):
    # print(("here").all())


if ((c>=a).all()) and ((c<=b).all()):
    print("hi")
