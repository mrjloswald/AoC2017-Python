class Node():
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def __str__(self):
        return self.name + " (" + str(self.weight) + ") " + self.childrenString() + " [" + str(self.totalWeight()) + "]"

    def __eq__(self, other):
        return self.name == other.name

    def childrenString(self):
        if self.hasChildren():
            return "-> " + ', '.join(map( lambda x: x.name, self.children))
        else:
            return ""

    def childrenWeights(self):
        if self.hasChildren():
            return [x.totalWeight() for x in self.children ] #list(map(lambda x: x.totalWeight(), children ))
        else:
            return 0

    def childrenWeight(self):
        if self.hasChildren():
            return sum( self.childrenWeights() )
        else:
            return 0

    def totalWeight(self):
        return self.weight + self.childrenWeight()

    def isBalanced(self):
        return self.childrenWeights()[1:] == self.childrenWeights()[:-1]
    # presupposes isBalanced = False
    def imbalancedChild(self):
        return self.children[len(self.children)-1]
        #return sorted(self.children, key= lambda child: child.totalWeight())[len(self.children)-1]

    def balancedChild(self):
        return self.children[0]
        #return sorted(self.children, key= lambda child: child.totalWeight())[0]

    def hasChildren(self):
        return len(self.children) > 0

nodes = {}
parents = []
children = []
for line in open("Day7_input.txt","r"):
    tokens = line.split()
    name = str(tokens[0])
    weight = int(line.split()[1][1:-1])
    nodes[name] = Node(name, weight, [])

for line in open("Day7_input.txt","r"):
    tokens = line.split()
    if len(tokens) > 2:
        node = nodes[str(tokens[0])]
        node.children = [nodes[child.strip(',')] for child in tokens[3:]]
        parents.append(node)
        children.extend(node.children)

for name, node in nodes.items():
    node.children.sort(key= lambda child: child.totalWeight())

for node in parents:
    if children.count(node) == 0:
        root = node

currentNode = root

while not currentNode.imbalancedChild().isBalanced():
    currentNode = currentNode.imbalancedChild()

print( currentNode.imbalancedChild().weight - (currentNode.imbalancedChild().totalWeight() - currentNode.balancedChild().totalWeight()))
