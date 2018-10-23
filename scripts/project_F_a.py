import numpy as np

# import data
# xmass = np.loadtxt(sys.argv[1])
f = open("datafiles/ups-15-small.bin","r")
datalist = np.fromfile(f,dtype=np.float32)

# number of events
nevent = len(datalist)/6
xdata = np.split(datalist,nevent)
print(xdata[0])

# make list of invariant mass of events
xmass = []
for i in range(0,nevent):
    xmass.append(xdata[i][0]/1000.)
    if i < 10:
        print(xmass[i])
