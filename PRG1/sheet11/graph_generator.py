class GraphGenerator:
    def __init__(self):
        self.graph: {[]} = dict()
        self.length = 0

    def setup_vertexes(self):
        num_vertexes = input(
            "Please enter the number of vertexes in your graph (integer).\n>>> ")
        if not num_vertexes.isdigit() or int(num_vertexes) < 2:
            print("Please enter an integer larger than one!")
            return self.setup_vertexes()
        num_vertexes = int(num_vertexes)
        self.length = num_vertexes

        for i in range(1, num_vertexes + 1):
            self.graph[str(i)] = []

    def setup_edges(self):
        print("Now you can enter connections between nodes.")
        print(
            f"Enter two numbers between 1 and {self.length} (space separated) to add an undirected connection.")
        print(
            f"Enter two numbers between 1 and {self.length} separated by '>' to add an directed connection.")
        print("Enter 'show' to visualize the current graph or 'done' to finish setting up edges.")
        curr_input = ""
        while True:
            curr_input = input(">>> ")
            if curr_input == 'show':
                self.show_graph()
            if curr_input == 'done':
                break
            input_list = curr_input.split(" ")
            if len(input_list) > 1:
                if len(input_list) > 2 or any(map(lambda x: x not in self.graph, input_list)):
                    print(
                        f"Please enter two number between 1 and {self.length} (space separated).")
                    continue
                self.add_undirected_connection(input_list[0], input_list[1])
                continue
            input_list = curr_input.split(">")
            if len(input_list) > 1:
                if len(input_list) > 2 or any(map(lambda x: x not in self.graph, input_list)):
                    print(
                        f"Please enter two number between 1 and {self.length} (space separated).")
                    continue
                self.add_directed_connection(input_list[0], input_list[1])

    def show_graph(self):
        print(self.graph)

    def add_undirected_connection(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def add_directed_connection(self, node1, node2):
        self.graph[node1].append(node2)

    @staticmethod
    def is_tree(graph):
        generator = GraphGenerator()
        generator.graph = graph
        return not generator.has_cycles() and generator.are_all_nodes_connected()

    def are_all_nodes_connected(self):
        for node in self.graph:
            if node != "1" and not self.are_nodes_connected("1", node):
                return False
        return True

    def has_cycles(self):
        for i in self.graph:
            if self.are_nodes_connected(i, i):
                return True
        return False

    def are_nodes_connected(self, start, end, visited_nodes=[], curr_node=None):
        if curr_node is None:
            curr_node = start
        visited_nodes = visited_nodes + [curr_node]
        for node in self.graph[curr_node]:
            if len(visited_nodes) == 2 and node == start:
                continue
            if node == end or (node not in visited_nodes
                               and self.are_nodes_connected(start, end, visited_nodes, node)):
                return True
        return False

    def are_nodes_adjacent(self, node1, node2):
        return node2 in self.graph[node1] or node1 in self.graph[node2]


if __name__ == "__main__":
    g = GraphGenerator()
    g.setup_vertexes()
    g.setup_edges()
    print("This graph is a tree/forest." if GraphGenerator.is_tree(g.graph)
          else "This graph is not a tree/forest.")
