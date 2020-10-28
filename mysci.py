# Initialize my data variable
# data = []  # list
# data = {}  # dictionary
data = {'date':[], 'time':[], 'tempout':[]}
time = data['time']

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

# Read the first three lines (header)
    for _ in range(3):
        datafile.readline()

# Changing data to columns
# dictionary

   # Read and parse the rest of the file
    for line in datafile:
#        datum = line.split()
#        data.append(datum)
         split_line = line.split() 
         data['date'].append(split_line[0])
         data['time'].append(split_line[1])
         data['tempout'].append(float(split_line[2]))
#  add of float() changes type to float, can do math on it now

# DEBUG
# print(data[0])
# print(data[9])
# print(data[-1])  # last data
# print(data[-2])  # 2nd to last data
# for datum in data[:10:2]:
#     print(data)
# print 9th item, 5th element
#print(data[8][4])
# print 9th item, first 6
#print(data[8][:5])
# print 9th item, but everyother one
#print(data[8][::2])
#
#print(data[5:8][0])
#print(data[5])

# Dictioniary
# print(data['time'])
print(data['tempout'])







