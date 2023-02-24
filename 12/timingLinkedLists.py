"""
This is a partial implementation of the LinkedList class and is used to
demonstrate that preprending (inserting at the front of a linked list
takes constant time regardless of the list's size. 
"""

from time import time

def main():
    size = 100
    trials = 10
    print("\ntesting indexing on LINKED lists")
    for i in range(8):
        avgIndexing(size, trials)
        size *= 2

    size = 100
    trials = 10
    print("\ntesting prepend on LINKED lists")
    for i in range(8):
        avgPrepending(size, trials)
        size *= 2

def timeIndexing(n):
    """
    Input: n, size of list to prepend to
    Return: time taken to index 1000 times
    """
    LL = buildLL(n)
    start = time()
    for i in range(1000):
        x = LL[n/2]
    end = time()
    return end-start

def avgIndexing(n, trials):
    """
    Input: n, size of list to test, number of trials to run
    Returns: none, prints results
    """
    total = 0.0
    for i in range(trials):
        total += timeIndexing(n)
    print("For LINKED list of size: %8d index time: [%.10f]" % 
          (n, total/trials))

def timePrepending(n):
    """
    Input: n, size of list to prepend to
    Return: time taken to append 1000 times
    """
    LL = buildLL(n)
    start = time()
    for i in range(1000):
        LL.prepend(22)
    end = time()
    return end-start

def avgPrepending(n, trials):
    """
    Input: n, size of list to test, number of trials to run
    Returns: none, prints results
    """
    total = 0.0
    for i in range(trials):
        total += timePrepending(n)
    print("For LINKED list of size: %8d prepend time: [%.10f]" % 
          (n, total/trials))

def buildLL(n):
    """
    Input: n, size of linked list to create
    Return: a new linked list of the given size
    """
    LL = LinkedList()
    for i in range(n):
        LL.append(i)
    return LL

class Node(object):
    """
    Repesents one element in a singly linked list.  A Node has two
    fields: data stores the data value(s) at the Node, and next refers
    to the next Node in the linked list.
    """
    
    def __init__(self, data):
        """
        Inputs:
          data -- the value of the Node
        Returns:
          None

        Purpose: Create an new linked list Node.
        """
        self.data = data
        self.next = None
        
    def __str__(self):
        """ 
        Inputs: None
        Returns: the string representation of a Node

        Purpose: Converts a Node to a string
        """
        result = "(%s)" % (self.data)
        if (self.next != None):
            result += "-->"
        else :
            result += "--|"
        return result

    def setData(self, data):
        """
        Inputs:
          data -- the value to assign to the Node's data field 
        Returns: None
        Purpose: Sets the data field of the Node.
        """
        self.data = data

    def setNext(self, next):
        """
        Inputs:
          next -- The next Node in the linked list or None if this Node
           is the end of the list
        Returns: None

        Purpose: Set the Node this Node points to.
        """
        self.next = next

    def getData(self):
        """
        Inputs: None
        Returns: the value of the data field for this Node. 

        Purpose: Gets the value of the Node.
        """
        return self.data

    def getNext(self):
        """
        Inputs: None
        Returns: a Node object which is the next Node in the linked list. 

        Purpose: Gets the next Node in the list.
        """
        return self.next

class LinkedList(object):
    """
    Represents a singly linked list.  A linked list has references to
    its head and tail node and maintains its current size
    """

    def __init__(self):
        """
        Create an empty linked list
        """
        self.head = None  # points to first Node in list
        self.tail = None  # points to last Node in the list
        self.size = 0     # number of elements in the list

    def __str__(self):
        """
        Create a string consisting of the content of linked list from
        front to back. Similiar to the string representation of the
        built-in Python list.

        Returns: a string representation of the linked list. 
        """
        result = "[" 
        current = self.head
        while current != None:
            result += "%s, " % (current.getData())
            current = current.getNext()
        if self.size > 0:
            result = result[:-2]
        result += "]"
        return result

    def __getitem__(self, index):
        """
        This function gets called when you index an item, e.g.,
        lst[index].  It should return the item at the index specfied.
        If the index is out of range or invalid, you should return
        None.

        Inputs:
          index -- the index in the linked list of the item to return

        Returns: the item in the Node at the index, or none if the
         index is invalid or out of bounds.
        """
        if index >= self.size:
            return None
        current = self.head
        for i in range(index):
            current = current.getNext()
        return current.getData()

    def append(self, item):
        """
        Inputs:  item -- the value to add to the linked list
        Returns: None
        Purpose: append item to the end of the linked list.
        """
        n = Node(item)
        if self.size == 0:
            self.head = n
        else:
            self.tail.setNext(n)
        self.tail = n
        self.size += 1
        
    def prepend(self, item):
        """
        Inputs:  item -- the value to add to the linked list
        Returns: None
        Purpose: Prepend item to the beginning of the linked list.
        """
        n = Node(item)
        if self.size == 0:
            self.tail = n
        else:
            n.setNext(self.head)
        self.head = n
        self.size += 1

main()
