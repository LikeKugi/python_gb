import sys
from typing import TypeVar

from Node import Node

_T = TypeVar('_T', bound='RedBlackTree')


class RedBlackTree:
    """
    Red Black Binary Tree
    """
    _TNULL = Node(None, color=2)  # Null node | Leaf

    def __init__(self: _T):
        self.root = self._TNULL

    def min(self: _T, node: Node) -> Node:
        """
        Find minimum node of a tree
        :param node: Node
        :return: Node
        """
        while node.left != self.TNULL:
            node = node.left
        return node

    def max(self: _T, node: Node) -> Node:
        """
        Find maximum of a tree
        :param node: Node
        :return: Node
        """
        while node.right != self.TNULL:
            node = node.right
        return node

    def delete(self: _T, value):
        self.__delete_node(self.root, value)

    def insert(self: _T, key):
        """
        insert value in tree
        :param key: Any
        :return: None
        """
        node = Node(key)
        node.left = self._TNULL
        node.right = self._TNULL
        self.__find_place_node(node)

    def left_rotate(self: _T, x: Node):
        """
        Left rotate of tree
        :param x: Node
        :return: None
        """
        y = x.right
        x.right = y.left
        if y.left != self._TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self: _T, x: Node):
        """
        Right rotate of tree
        :param x: Node
        :return: None
        """
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __find_place_node(self: _T, node: Node):
        """
        place node
        :param node: Node
        :return: None
        """
        y = None
        x = self.root

        while x != self._TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 2
            return

        if node.parent.parent is None:
            return
        self.__fix_insert(node)

    def __delete_node(self: _T, node: Node, key) -> bool:
        """
        Delete node with data of key
        :param node: Node
        :param key: any - Node.data of deleting Node
        :return: None
        """
        z = self._TNULL
        while node != self._TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self._TNULL:
            print(f'No such value in a tree {key}')
            return False

        y = z
        y_original_color = y.color_value()
        if z.left == self._TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self._TNULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.min(z.right)
            y_original_color = y.color_value()
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 2:
            self.__fix_delete(x)

    def __rb_transplant(self: _T, u: Node, v: Node):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __delete_node_helper(self: _T, node: Node, key):
        z = self._TNULL
        while node != self._TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self._TNULL:
            print(f'No such value in a tree {key}')
            return False

        y = z
        y_original_color = y.color_value()
        if z.left == self._TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self._TNULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color_value()
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 2:
            self.__fix_delete(x)

    def __fix_delete(self: _T, x: Node):
        while x != self.root and x.color_value() == 2:
            if x == x.parent.left:
                s = x.parent.right
                if s.color_value() == 1:
                    s.color = 2
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color_value() == 2 and s.right.color_value() == 2:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color_value() == 2:
                        s.left.color = 2
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 2
                    s.right.color = 2
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color_value() == 1:
                    s.color = 2
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color_value() == 2 and s.right.color_value() == 2:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color_value() == 2:
                        s.right.color = 2
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color_value()
                    x.parent.color = 2
                    s.left.color = 2
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 2

    def print(self: _T):
        self.__print_helper(self.root, "", True)

    def __print_helper(self, node, indent, last):
        if node != self._TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(f'{node.data} ({node.color})')
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def __pre_order_helper(self, node):
        if node != self._TNULL:
            sys.stdout.write(node.data + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != self._TNULL:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != self._TNULL:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.stdout.write(node.data + " ")

    def __search_tree_helper(self, node, key):
        if node == self._TNULL or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    def __fix_insert(self, k):
        while k.parent.color_value() == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color_value() == 1:
                    u.color = 2
                    k.parent.color = 2
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 2
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color_value() == 1:
                    u.color = 2
                    k.parent.color = 2
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 2
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 2




if __name__ == "__main__":
    bst = RedBlackTree()
    bst.insert(8)
    bst.insert(18)
    bst.insert(5)
    bst.insert(15)
    bst.insert(17)
    bst.insert(25)
    bst.insert(40)
    bst.insert(80)
    bst.delete(25)
    bst.print()
