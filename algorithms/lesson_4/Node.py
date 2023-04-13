from __future__ import annotations


class Node:

    def __init__(self, val: int):
        self.value = val
        self.next = None
        self.prev = None

    def pushNext(self, node: Node):
        self.next = node
        node.prev = self

    def pushPrev(self, node: Node):
        self.prev = node
        node.next = self

    def popNode(self):
        self.next = None
        self.prev = None

    def popNext(self):
        self.next = None

    def popPrev(self):
        self.prev = None

    def __repr__(self):
        return f'Node({self.value})'