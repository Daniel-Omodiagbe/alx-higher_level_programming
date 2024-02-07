#!/usr/bin/python3
"""this module defines a singly linked list"""


class Node:
    """the base class for the node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """instantiation of attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the attribute data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves the attribute next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the attribute next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines the class singly linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        """to print out all elements of the linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)

    def sorted_insert(self, value):
        """inserts new Node into the singly linked list"""
        node = Node(value)
        if self.__head is None or self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            node.next_node = tmp.next_node
            tmp.next_node = node
