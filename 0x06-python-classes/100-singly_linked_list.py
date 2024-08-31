#!/usr/bin/python3
""" a linked list oop """


class Node:
    """ defines a node for a singly linked list"""
    def __init__(self, data, next_node=None):
        """ initialization method"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """ set data parameter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ get next_node property"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ singly linked list class"""
    def __init__(self):
        """ initialization"""
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new node """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """ representation of the object"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))i
