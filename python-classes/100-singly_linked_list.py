#!/usr/bin/python3
"""
This module defines a Node and a SinglyLinkedList class.
"""


class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Gets the data value of the node.
        """
        return self.__data

    @property
    def next_node(self):
        """
        Gets the next node in the list.
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list.
        """
        if isinstance(value, (Node, type(None))):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        node_list = ""
        head = self.__head
        while head:
            node_list += f"{str(head.data)}"
            if head.next_node:
                node_list += "\n"
            head = head.next_node

        return node_list

    def sorted_insert(self, value):
        """
        Inserts a new Node into the list in the correct sorted position.

        """
        new_node = Node(value, self.__head)

        if not self.__head:
            self.__head = new_node
            return

        if not self.__head.next_node:
            if new_node.data <= self.__head.data:
                self.__head = new_node
            else:
                new_node.next_node = None
                self.__head.next_node = new_node
            return
        else:
            if new_node.data <= self.__head.data:
                self.__head = new_node
                return

        head = self.__head
        while True:
            if not head.next_node:
                head.next_node = new_node
                new_node.next_node = None
                return

            if new_node.data <= head.next_node.data:
                new_node.next_node = head.next_node
                head.next_node = new_node
                return

            head = head.next_node
