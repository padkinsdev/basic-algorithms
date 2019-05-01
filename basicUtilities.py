# library that contains the algorithms and
# data types that are being tested

class SortableList(list):
  def __init__(self, elements):
    super(SortableList, self).__init__(elements)

  def randomize(self):
    for i in range(0, len(self)):
      secondLocation = (self[i]^i)%len(self)
      self.swap(i, secondLocation)

  def swap(self, indexOne, indexTwo):
    # utility function for swapping two values in a list
    tempVal = self[indexOne]
    self[indexOne] = self[indexTwo]
    self[indexTwo] = tempVal

# Algorithms:

  def insertionSort(self):
    for index in range(1, len(self)):
      i = index
      tempVal = self[index]
      while (tempVal < self[i-1] and i > 0):
        self[i] = self[i-1]
        i -= 1
      self[i] = tempVal
    return self

  def selectionSort(self):
    for index in range(0, len(self)-1):
      minValIndex = index
      for i in range(index, len(self)):
        if (self[minValIndex] > self[i]):
          minValIndex = i
      self.swap(index, minValIndex)
    return self

  def bubbleSort(self):
    cleanPass = False # cleanPass represents whether the algorithm has gone through the list without switching any elements in it
    while (not cleanPass):
      cleanPass = True
      for index in range(1, len(self)):
        if (self[index-1] > self[index]):
          cleanPass = False
          self.swap(index-1, index)
    return self

# When sorting an array of randomly arranged numbers on the range [0,10000], selectionSort() appeared to 


# Data Structures:

class Queue:
  def __init__(self):
    self._tasks = []
    # queues follow first in, first out functioning
  def enqueue(self, newTask):
    self._tasks.append(newTask)
  def dequeue(self):
    if (len(self._tasks) < 1):
      raise IndexError("No tasks in queue")
    taskToPop = self._tasks[0]
    for i in range(1, len(self._tasks)):
      self._tasks[i-1] = self._tasks[i]
    self._tasks.pop()
    return taskToPop

class Stack:
  def __init__(self):
    self._items = []
    # stacks follow first in, last out functioning
  def pushItem(self, newItem):
    self._items.append(newItem)
  def popItem(self):
    itemToPop = self._items[len(self._items)-1]
    self._items.pop()
    return itemToPop

class SingleLinkedList:
  def __init__(self):
    self._storage = [["null", -1]]
  def addNewLink(self, value):
    #finalLinkLocation = self._storage[0][1]
    index = 0
    while (self._storage[index][1] != -1):
      # finds the location of the last element in the list
      index = self._storage[index][1]
    self._storage.append([value, -1])
    self._storage[index][1] = self.findLength(self._storage)
  def findLength(self):
    pointer = 0
    numLinks = 0
    while (self._storage[pointer][1] != -1):
      pointer = self._storage[pointer][1]
      numLinks += 1
    return numLinks
  def changeTo(self, entryNumber, value):
    # changes the entryNumber'th stored value to the value passed to the function
    if (self._storage.findLength() < entryNumber):
      raise IndexError("Linked list contains " + str(self._storage.findLength()) + " elements. Attempted to access element number " + str(entryNumber) + ".")
    else:
      pointer = self._storage[0][1]
      linkNum = 1
      while (linkNum < entryNumber):
        pointer = self._storage[pointer][1]
        linkNum += 1
      self._storage[pointer][0] = value
  def getValue(self, entryNumber):
    if (self._storage.findLength() < entryNumber):
      raise IndexError("Linked list contains " + str(self._storage.findLength()) + " elements. Attempted to access element number " + str(entryNumber) + ".")
    else:
      pointer = self._storage[0][1]
      linkNum = 1
      while (linkNum < entryNumber):
        pointer = self._storage[pointer][1]
        linkNum += 1
      return self._storage[pointer][0]
  def deleteElement(self, entryNumber):
    if (self._storage.findLength() < entryNumber):
      raise IndexError("Linked list contains " + str(self._storage.findLength()) + " elements. Attempted to access element number " + str(entryNumber) + ".")
    else:
      pointer = self._storage[0][1]
      linkNum = 1
      while (linkNum < entryNumber-1):
        pointer = self._storage[pointer][1]
        linkNum += 1
      self._storage[pointer][1] = self._storage[self._storage[pointer][1]][1]
      # unlinks the desired element from the chain of list elements
      return self._storage[pointer][0]
