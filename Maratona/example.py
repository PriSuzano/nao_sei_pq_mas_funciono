class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()




------------------------

n,k = map(int , input().split())

superiores = list(map(int , input().split())) #1 1 2 3 4 4 6
# subordinados = []
# for i in range(n-1):
#     subordinados.append(i+1)


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.left = None
        self.right = None

    def insert(self, value, sub=None):

        if self.value!=value:
            self.value = self.left

        print(self.value, value, sub)
        # if self.left is not None:
        #     print(self.left.value)

        if value!=sub:
            if self.left is None:
                print('left')
                self.left = Node(sub)
            elif self.right is None:
                print('right')
                self.right = Node(sub)
            else:
                self.left.insert(sub)
            print('\n')

    def print(self):
        if self.left:
            self.left.print()

        if(self.right):print(self.right.value, end="")
        print(self.value, end="")
        if(self.left):print(self.left.value)
        print('\n')
        
        if self.right:
            self.right.print()


root = Node(1)
for i,elem in enumerate(superiores):
    root.insert(elem, i+1)

#root.print()