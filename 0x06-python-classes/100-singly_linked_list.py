#!/usr/bin/python3
"""istantiates a class node"""


class node:
    """defines a class node"""

    def __init__(self, data, next_node=None):
        """initializes node with its attributes"""

        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """getter for data"""

            return self.__data

        @data.setter
        def data(self, value):
            """setter for data"""

            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """gettert for node"""

            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """setter for next node"""

            if (value is not None and not isinstance(value, node)):
                raise TypeError("next_node must be a node object")

            self.__next_node = value


class SinglyLinkedList:
    """instantiates a singly linked list class"""

    def __init__(self):
        """intializes the singly linked list"""

        self.head = None

    def __str__(self):
        """ pprints the list"""

        print_all = ""
        position = self.head
        while position:
            print_all += str(position.data) + "\n"
            position = position.next_node
        return print_all[:-1]

    def sorted_insert(self, value):
        """inserts sorted values"""

        new = node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        position = self.head
        while position.next_node and position.next_node.data < value:
            position = position.next_node
        if position.next_node:
            new.next_node = position.next_node
        position.next_node = new
