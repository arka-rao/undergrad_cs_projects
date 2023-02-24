"""
linkedList.py

A linked list implementation. 

Author: Your Name
Date: The date

"""

def main():
    LL = LinkedList()
    LL.append(10)
    print LL
    LL.append(20)
    print LL
    LL.append(30)
    print LL
    LL.prepend(5)
    print LL

    """
    #test code for linkedlist
    n1 = Node(12)
    n2 = Node(15)
    n3 = Node(20)
    n1.setNext(n2)
    n2.setNext(n3)
    current = n1
    result = ""
    while current != None:
        result += str(current)
        current = current.getNext()
    print result
    """
    
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

    def __len__(self):
        """
        Gets the length of the list.

        Returns: the length of the list.
        """
        return self.size
        
        
    def __contains__(self, item):
        """
        Inputs:
          item -- the item to look for in the list

        Returns: True if the item is in the list, False otherwise

        Purpose: 
          The method that implements the 'in' keyword for the linked list.
        """
        pass

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
        pass

    def __setitem__(self, index, item):
        """
        This function gets called when you update an item in the list,
        e.g., lst[index] = 10.  If the index is out of range or
        invalid, simply return without updating anything.
        
        Inputs:
          index -- the index in the linked list of the item to updat
          item -- the new item to put at index. 
        Returns: None
        """
        pass

    def append(self, item):
        """
        Inputs:
          item -- the value to add to the linked list
        Returns: None

        Purpose: Append item at the end of the linked list.

        This method creates a new Node that it will add to the end of
        the linked list.
        """
        #step 1 - make a new node to hold item
        #step 2 - if list is empty, set head and tail to new node
        #else, set tail's next to new node, then set tail to new node
        #step 3 - finally, increment size

        n = Node(item)
        if self.size == 0:
            self.head = n
        else:
            self.tail.setNext(n)
        self.tail = n
        self.size += 1
        
        
    def prepend(self, item):
        """
        Inputs:
          item -- the value to add to the linked list
        Returns: None

        Purpose: Prepend date to the begining of the linked list.

        This method creates a new Node that it will add to the front
        of the linked list
        """
        #step 1 - create a new node
        #step 2 - if empty list, set head and tail to new node
        #step 3 - else, change n's next to what head is, and set head to new node
        n = Node(item)
        if self.size == 0:
            self.tail = n
        else:
            n.setNext(self.head)
        self.head = n
        self.size += 1
            
        
        
    def removeFromHead(self):
        """
        Inputs: None
        Returns: 
          the value of the removed node or None if the list is empty

        Purpose: Removes the element from the front of the list.
        """
        pass

    def removeFromTail(self):
        """
        Inputs: None
        Returns: 
          the value of the removed node or None if the list is empty

        Purpose: Removes the element from the end of the list.
        """
        pass

    def count(self, item):
        """
        Inputs:
          item -- the item to look for.
        Returns: The number of times item apears in the list.  If the
        item doesn't appear in the list, return 0.

        Purpose: Return the number of nodes matching item in the list.
        """
        pass

    def index(self, item):
        """
        Inputs:
          item -- the value to search for in the list

        Returns: The index of the first Node with the matching value
        or None if the value isn't present in the list. 

        Purpose: Find a node with the matching item in the list.
        """
        pass

    def insert(self, index, item):
        """
        Inputs:
          index -- the place in the list to add the item
          item -- the element to place in the list at the index

        Returns:
          True if the item was inserted successfully, False if the item
            could not be inserted.

        Purpose:
          Insert item into the linked list at index.
          If the index is negative, do not insert.
          If the index is greater than the current size, add the item
            to the end of the list.
        """
        pass

    def remove(self, item):
        """
        Inputs:
          item -- the value to search for in the list

        Returns: True if a node was removed from the list or False if
        the item could not be removed from the list.

        Purpose: Delete the first Node with the item in the list.
        """
        pass

    def pop(self, index):
        """
        Inputs:
          index -- the index of the item to remove

        Returns: The item removed or None if the index is invalid or
        out of range.

        Purpose: Remove and return the item at index.  If the list is
        empty or index is out of range, return None
        """
        pass

def unitTests():
    # Test the constructor __init__, __str__ method
    print("****Testing Constructor****")
    lst = LinkedList()
    print("Test01 %s []" % str(lst))
    assert(str(lst) == "[]")
    print("Constructor test passed!!")

    # Test append
    print("\n****Testing append method****")
    lst.append(2)
    print("Test02 %s [2]" % str(lst))
    lst.append(3)
    print("Test03 %s [2,3]"  % str(lst))

    # Test04 uses public data members, but just for testing purposes
    print("Test04 lst.size = %d 2" % lst.size)


    # Test prepend
    print("\n****Testing prepend method****")
    lst = LinkedList()
    lst.prepend(0)
    print("Test05 %s [0]" % str(lst))
    lst.prepend(1)
    print("Test06 %s [1, 0]" % str(lst))
    print("Test07 lst.size = %d 2" % lst.size)
    lst.append(2)
    print("Test08 %s [1, 0, 2]" % str(lst))

    # Test insert
    print("\n****Testing insert method****")
    lst = LinkedList()
    lst.insert(1,1)
    print("Test09 %s [1]" % str(lst))
    lst.insert(0,0)
    print("Test10 %s [0, 1]" % str(lst))
    lst.insert(2,3)
    print("Test11 %s [0, 1, 3]" % str(lst))
    lst.insert(2,2)
    print("Test12 %s [0, 1, 2, 3]" % str(lst))
    lst.insert(-1,-1)
    print("Test13 %s [0, 1, 2, 3]" % str(lst))
    print("Test14 lst.size = %d 4" % lst.size)


    # Test count
    print("\n****Testing count method****")
    print("Test15 lst.count(2) = %d 1" % lst.count(2))
    print("Test16 lst.count(200) = %d 0" % lst.count(200))
    lst.append(2)
    print("Test17 lst.count(2) = %d 2" % lst.count(2))

    # Test index
    print("\n****Testing index method****")
    print("Test18 lst.index(2) = %d 2" % lst.index(2))
    print("Test19 lst.index(10) = %s None" % lst.index(10))

    # Test remove methods
    print("\n****Testing remove method****")
    print("Test20 lst.remove(0) = %s True" % lst.remove(0))
    print("Test21 lst.remove(0) = %s False" % lst.remove(0))
    print("Test22 lst.removeFromHead() = %d 1" % lst.removeFromHead())
    print("Test23 lst.removeFromTail() = %d 2" % lst.removeFromTail())
    print("Test24 lst.size = %d 2" % lst.size)
    lst = LinkedList()
    print("Test25 lst.removeFromTail = %s None" % lst.removeFromTail())
    lst.append(1)
    lst.append(2)
    print("Test26 lst.removeFromTail = %s 2" % lst.removeFromTail())
    print("Test27 lst.size = %d 1" % lst.size)
    lst = LinkedList()
    print("Test28 lst.removeFromHead(empty) = %s None" % lst.removeFromHead())
    lst.append(1)
    lst.append(2)
    print("Test29 lst.removeFromHead = %d 1" % lst.removeFromHead())
    print("Test30 lst.removeFromHead = %d 2" % lst.removeFromHead())
    print("Test31 lst.size = %d 0" % lst.size)
    lst = LinkedList()
    for i in range(5):
        lst.append(i)
    print("Test32 lst = %s [0, 1, 2, 3, 4]" % lst)
    print("Test33 lst.remove(2) = %s True" % lst.remove(2))
    print("Test34 lst = %s [0, 1, 3, 4]" % lst)
    print("Test35 lst.remove(2) = %s False" % lst.remove(2))

    # Test pop
    print("\n****Testing pop method****")
    lst = LinkedList()
    lst.append(0)
    lst.append(1)
    lst.append(3)
    print("Test36 lst.pop(0) = %d 0" % lst.pop(0))
    print("Test37 lst = %s [1, 3]" % lst)
    print("Test38 lst.size = %d 2" % lst.size)
    print("Test39 lst.pop(10) = %s None" % lst.pop(10))
    print("Test40 lst = %s [1, 3]" % lst)
    print("Test41 lst.size = %d 2" % lst.size)
    print("Test42 lst.pop(1) = %d 3" % lst.pop(1))
    print("Test43 lst = %s [1]" % lst)
    print("Test44 lst.pop(0) = %d 1" % lst.pop(0))
    print("Test45 lst = %s []" % lst)
    print("Test46 lst.size = %d 0" % lst.size)

    # Test insert
    print("\n****Testing insert method****")
    lst = LinkedList()
    for i in range(5):
        lst.insert(0,i)
    print("Test47 lst.size = %d 5" % lst.size)
    print("Test48 lst = %s [4, 3, 2, 1, 0]" % lst)

    # Test contains method
    print("\n****Testing contains method****")
    print("Test49 <5 in lst> %s False" % (5 in lst))
    print("Test50 <2 in lst> %s True" % (2 in lst))
    lst = LinkedList()
    print("Test51 <5 in empty lst> %s False" % (5 in lst))
    print("Test52 <2 in empty lst> %s False" % (2 in lst))
    

    # Test element access/setting: __getItem__, __setItem__ 
    print("\n****Testing element access****")
    lst = LinkedList()
    for i in range(5):
        lst.append(i)
    print("Test53 lst = %s [0, 1, 2, 3, 4]" % lst)
    print("Test54 lst[0] = %d 0" % lst[0])
    print("Test55 lst[100] = %s None" % lst[100])
    lst[0] = 100
    print("Test56 lst[0] = 100; lst = %s [100, 1, 2, 3, 4]" %
          lst)
    lst[100] = 200
    print("Test57 lst[100] = 200; lst = %s [100, 1, 2, 3, 4]" %
          lst)
    
if __name__ == "__main__":
  main()
