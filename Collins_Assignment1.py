__author__ = 'Zak Collins'

import Queue


class MyQueue:
    def __init__(self):
        self.q = Queue.Queue()

    def put(self, i):
        self.q.put(int(i))

    def get(self):
        return self.q.get()

    def qsize(self):
        return self.q.qsize()

    def empty(self):
        return self.q.empty()

    def full(self):
        return self.q.full()


class MyStack:
    def __init__(self):
        self.l = []

    def push(self, i):
        self.l.append(i)

    def pop(self):
        return self.l.pop()

    def checkSize(self):
        return len(self.l)


class MyBinaryTree:
    def __init__(self):
        self.root = MyTreeNode(0, None)

    def add(self, value, parentValue):
        parent = self.findValue(parentValue, self.root)
        if parent == None:
            print "Parent not found"
            return
        newNode = MyTreeNode(value, parent)
        if parent.left == None:
            parent.left = newNode
        elif parent.right == None:
            parent.right = newNode
        else:
            print "Parent has two children, node not added"

    def delete(self, value):
        node = self.findValue(value, self.root)
        if node == None:
            print "Node not found"
        elif node.right != None or node.left != None:
            print "Node not deleted, has children"
        else:
            if node.parent.left == node:
                node.parent.left = None
            elif node.parent.right == node:
                node.parent.right = None
            node.parent = None

    def Print(self):
        self.printTree(self.root)

    def printTree(self, node):
        if node != None:
            print node.key
            self.printTree(node.left)
            self.printTree(node.right)

    def findValue(self, value, node):
        if node == None:
            return None
        if value == node.key:
            return node
        nodeLeft = self.findValue(value, node.left)
        nodeRight = self.findValue(value, node.right)

        if nodeLeft != None:
            return nodeLeft
        elif nodeRight != None:
            return nodeRight
        else:
            return None


class MyTreeNode:
    left = None
    right = None
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent


class MyGraph:
    def __init__(self):
        self.dict = {}

    def addVertex(self, value):
        if value in self.dict.keys():
            print 'Vertex already exists'
        else:
            self.dict[value] = []

    def addEdge(self, value1, value2):
        if self.dict[value1].count(value2) != 0:
            print 'Edge already exists, not added'
        elif value1 in self.dict.keys() and value2 in self.dict.keys():
            self.dict[value1].append(value2)
            self.dict[value2].append(value1)
        else:
            print 'One or more vertices not found'

    def findVertex(self, value):
        if value in self.dict.keys():
            print self.dict[value]


def main():
    print 'My Queue:'
    q = MyQueue()
    for x in range(1, 11):
        q.put(x)
    for x in range(1, 11):
        print q.get()

    print ''
    print 'My Stack:'
    s = MyStack()
    for x in range(1, 11):
        s.push(x)
    print 'Size: ', s.checkSize()
    for x in range(1, 11):
        print s.pop()

    print ''
    print 'My Tree:'
    t = MyBinaryTree()
    t.add(1, 0)
    t.add(2, 0)
    t.add(3, 1)
    t.add(4, 1)
    t.add(5, 2)
    t.add(6, 2)
    t.add(7, 3)
    t.add(8, 3)
    t.add(9, 4)
    t.add(10, 4)
    print 'Tree:'
    t.Print()
    t.delete(8)
    t.delete(10)
    print ''
    print 'Tree After Deletion: '
    t.Print()

    print ''
    print 'My Graph:'
    g = MyGraph()
    for x in range(1, 11):
        g.addVertex(x)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(1, 5)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 7)
    g.addEdge(6, 8)
    g.addEdge(6, 9)
    g.addEdge(6, 10)
    g.addEdge(7, 8)
    g.addEdge(7, 9)
    g.addEdge(7, 10)
    g.addEdge(8, 9)
    g.addEdge(8, 10)
    g.addEdge(9, 10)
    for x in range(1, 11, 2):
        g.findVertex(x)


main()