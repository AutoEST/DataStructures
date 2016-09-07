import datetime


class PyList1:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]  # simply add a list with a single value (item) to the items list


class PyList2:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)  # use the built in list.append function


class PyList3:
    def __init__(self, size=1):
        self.items = [None] * size
        self.numItems = 0

    def append(self, item):  # use the large array "placeholder" (this is faster todo: explain why)
        if self.numItems == len(self.items):  # if count of items in 'items' list is equal to the value of numItems
            newlst = [None] * self.numItems * 2  # create a new list with that is twice the size of the total number of items
            for k in range(len(self.items)):  # loop through the list 'items'
                newlst[k] = self.items[k]  # assign a value at k of the 'items' list to an item at k of 'newlst'
            self.items = newlst  # set all the values of the 'items' list to the same values of 'newlst'
        self.items[self.numItems] = item
        self.numItems += 1


def write_pylist(p1x, p1y, p2x, p2y, p3x, p3y):

    # Write an XML file with the results
    file = open("ListAccessTiming.xml", "w")
    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    file.write('<Plot title="Average List Element Access Time">\n')

    file.write(' <Axes>\n')
    file.write('   <XAxis min="' + str(0) + '" max="' + str(len(p1x)) + '">List Size</XAxis>\n')
    file.write('   <YAxis min="' + str(0) + '" max="' + str(max(p1y)) + '">Microseconds</YAxis>\n')
    file.write(' </Axes>\n')

    # p1
    file.write(' <Sequence title="Average Access Time PyList1" color="red">\n')

    for i in range(len(p1x)):
        file.write('   <DataPoint x="' + str(p1x[i]) + '" y="' + str(p1y[i]) + '"/>\n')

    file.write(' </Sequence>\n')

    # p2
    file.write(' <Sequence title="Average Access Time PyList2" color="blue">\n')

    for i in range(len(p2x)):
        file.write('   <DataPoint x="' + str(p2x[i]) + '" y="' + str(p2y[i]) + '"/>\n')

    file.write(' </Sequence>\n')

    # p3
    file.write(' <Sequence title="Average Access Time PyList3" color="green">\n')

    for i in range(len(p3x)):
        file.write('   <DataPoint x="' + str(p3x[i]) + '" y="' + str(p3y[i]) + '"/>\n')

    file.write(' </Sequence>\n')

    file.write('</Plot>\n')
    file.close()


def main():
    p = PyList3()
    xList = [0]
    yList = [0]
    starttime = datetime.datetime.now()
    for k in range(64):
        xList.append(k)
        for j in range(1024):
            p.append(j)
        yList.append((datetime.datetime.now() - starttime).total_seconds() * 1000)
    p3xList = xList
    p3yList = yList

    print(yList)
    p2 = PyList2()
    xList = [0]
    yList = [0]
    starttime = datetime.datetime.now()
    for k in range(64):
        xList.append(k)
        for j in range(1024):
            p2.append(j)
        yList.append((datetime.datetime.now() - starttime).total_seconds() * 1000)

    p2xList = xList
    p2yList = yList
    print(yList)
    p1 = PyList1()
    xList = [0]
    yList = [0]
    starttime = datetime.datetime.now()
    for k in range(64):
        xList.append(k)
        for j in range(1024):
            p1.append(j)
        yList.append((datetime.datetime.now() - starttime).total_seconds() * 1000)
    p1xList = xList
    p1yList = yList

    print(yList)

    write_pylist(p1xList, p1yList, p2xList, p2yList, p3xList, p3yList)

if __name__ == "__main__":
    main()
