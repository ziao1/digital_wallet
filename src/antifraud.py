### Read txt file
import csv
batch_reader = csv.reader(open('./paymo_input/batch_payment.txt','rU'), dialect=csv.excel_tab)
batch = list(batch_reader)


### Split each string by comma
for i in range(len(batch)):
    batch[i] = [x.strip() for x in batch[i][0].split(',')]


### Only keep rows that have at least 5 rows
### Delete "bad" rows which only contain comments
batch_new = []
for i in range(len(batch)):
    if (len(batch[i])>=5):
        batch_new.append(batch[i])


### Create input data which is list of tuples containing ids
inputdata = [None] * len(batch_new)
for i in range(len(batch_new)):
    inputdata[i] = (batch_new[i][1], batch_new[i][2])


### Drop the first row which contains id1 and id2
inputdata.pop(0)


from collections import defaultdict

### Create the Graph using a new class
### The default graph is an undirected graph
class Graph(object):
    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Initial connection by adding points in each tuple """
        for point1, point2 in connections:
            self.add(point1, point2)

    def add(self, point1, point2):
        """ Add connection of point1 and point2 """
        self._graph[point1].add(point2)
        if not self._directed:
            self._graph[point2].add(point1)

    def is_connected(self, point1, point2):
        """ Check if point1 is connected to point2 """
        return point1 in self._graph and point2 in self._graph[point1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


### Prepare input to construct graph
connections = inputdata
g = Graph(connections)
graph = g._graph


### Implement of Breadth First Search Algorithm
### Used to find shortest path between two nodes

### Read Test data
import csv
stream_reader = csv.reader(open('./paymo_input/stream_payment.txt','rU'), dialect=csv.excel_tab)
stream = list(stream_reader)


### Split each string by comma
for i in range(len(stream)):
    stream[i] = [x.strip() for x in stream[i][0].split(',')]


### Only keep rows that have at least 5 rows
### Delete "bad" rows which only contain comments
stream_new = []
for i in range(len(stream)):
    if (len(stream[i])>=5):
        stream_new.append(stream[i])


### Create test input data which are two lists containing ids
start_data = [None] * len(stream_new)
end_data = [None] * len(stream_new)
for i in range(len(stream_new)):
    start_data[i] = stream_new[i][1]
    end_data[i] = stream_new[i][2]


### Drop the first row which contains id1 and id2
start_data.pop(0)
end_data.pop(0)


### Test data using Graph constructed
### Three outputs
### output 1: have direct payments
### output 2: 2nd degree friend
### outptu 3: 4th degree friend

# Create list with default unverified
output1 = ['unverified'] * len(stream_new)
output2 = ['unverified'] * len(stream_new)
output3 = ['unverified'] * len(stream_new)
for i in range(len(start_data)):
    # print index every 1000 iterations
    if i%1000 ==0:
        print i
    # identify new ids as untrusted
    if len(graph[start_data[i]]) == 0:
        output1[i] = 'unverified'
        output2[i] = 'unverified'
        output3[i] = 'unverified'
    # identify direct payments as trusted for all outputs
    elif end_data[i] in graph[start_data[i]]:
        output1[i] = 'trusted'
        output2[i] = 'trusted'
        output3[i] = 'trusted'
    # identify 2nd degree friend as trusted for output2 and output 3
    elif end_data[i] in friendlist[start_data[i]]:
        output2[i] = 'trusted'
        output3[i] = 'trusted'
    # identify 4th degree friend as trusted for output 3
    else:
        for element in friendlist[start_data[i]]:
            if end_data[i] in friendlist[element]:
                output3[i] = 'trusted'


### Save outputs as txt files
file1 = open('./paymo_output/output1.txt', 'w')
for item in output1:
    file1.write("%s\n" % item)
file1.close()

file2 = open('./paymo_output/output2.txt', 'w')
for item in output2:
    file3.write("%s\n" % item)
file2.close()

file3 = open('./paymo_output/output3.txt', 'w')
for item in output3:
    file3.write("%s\n" % item)
file3.close()
















