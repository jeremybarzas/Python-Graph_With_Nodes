'''node module to use '''


class Node(object):

    '''The Node object'''

    def __init__(self, identifier, val):
        self._identifier = identifier
        self._value = val

    def print_info(self):
        '''abc'''
        print "ID:", self._identifier, ", Value:", self._value


class Graph(object):
    ''' The Graph object'''

    def __init__(self, n, x, y):
        self._nodes = n
        self._xsize = x
        self._ysize = y


def get_node(indentifier, graph):
    ''' Returns the node with the given id within the given graph'''
    for node in graph._nodes:
        if node._identifier == indentifier:
            return node
    return Node(id, "No node with this id found.")


def get_neighbors(node, graph):
    '''Gets the neighbors of the given node within the given graph'''
    print "get_neighbors() was called."
    tmpnode = get_node(node._identifier, graph)


def main():
    ''' main body function'''
    print "This is the main function."
    nodelist = [Node(0, 'A'), Node(1, 'B'), Node(2, 'C')]
    graph = Graph(nodelist, 3, 3)
    node = get_node(0, graph)
    node.print_info()
    node = get_node(1, graph)
    node.print_info()
    node = get_node(2, graph)
    node.print_info()
    node = get_node(9, graph)
    node.print_info()

if __name__ == "__main__":
    main()
