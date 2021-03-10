from numpy import loadtxt
datapath = open("diabetes.csv", 'r')
data = loadtxt(datapath, delimiter=",", skiprows=1)
print(data.shape)
print(data[:3])