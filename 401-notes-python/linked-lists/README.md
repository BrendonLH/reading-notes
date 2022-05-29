# Linked Lists
 - also include Big O article

## Big O: Analysis of Algorithm Efficiency

- Big O is used to describe the efficiency of an algorithm/function/data structure. There are two factors that makeup Big O
 > Running Time
 - Time Complexity
    - how long it takes to complete
 
 > Memory Space
 - Space Complexity
    - how much memory/space a algorithm/ function takes up.

there are 4 areas to consider when analyzing for time and space complexity.

1. Input size
    - the size of the parameter values such as (n)
    - lists/arrays are a good example, input size is determined by the size of the array/list. The more elements, the bigger the input size (memory/space).
2. Units of Measurment
    > Running Time
    - Time in Milliseconds, the measurement of how long it takes the function/algorithm to run
    - Number of operations that are executed (number of lines of code that are run)
     - Number of Basic Operations, the operation that contributes the most, this is the most time consuming in a function/algorithm
    > Memory Space
    - Amount of space needed to hold the code
    - amount of space needed to hold the input data(lists/arrays)
    - Amount of space needed for output data
    - Amount of space needed for the actual working space such as stack space, creation of variables and reference points.
3. Orders of Growth
    - we can describe overall efficiency by using (n) - input size, and measuring the Units of **Space and Time** that are needed.
    - As (n) grows, so does our time and space complexity.
4. Best Case, Worst Case, Average Case


> Constant Complexity
 - all inputs used will always use the same amount of Time and Space
 - this has an O(1) constant efficiency nomatter the size of the input.

> Logarithmic Complexity
 - the greater the value of the input(n) the rate of complexity decreases as it grows. An example would be a Binary Search.

> Linear Complexity
 - the size of inputs(n) will directly determine the amount of Memory and time.

 ## Linked Lists
> what is a Linked list? 
 - a series of nodes that are connected  to each other using **next**
 - there are two types:
    - Singly
        - only one reference or direction
        - (node)*--next-->*(node)*--next-->*(node)
    - Doubly
        - two references, one reference that points to the next node, and the other to point to the previous node
        - (node)*<--previous/next-->*(node)*<--previous/next-->*(node)
    
> Example
    ![Linked-list-Types](/401-notes-python/linked-lists/img/Untitled%20Diagram.drawio%20(2).png)


## Example/How to

> Insert node at end of linked list




    class Node: 
        def __init__(self, data):
        seld.data = data
        self.next = None
    class Linked_List:
        def __init__(self):
        self.head = None

    def insert_node_end(self, new_element):
        new_node = Node(new_element)
        if self.head = None:
            self.head = new_node
            return
        end_node = self.head
        while (end_node.next):
            end_node = end_node.next
        
        end_node.next = new_node

     
    

