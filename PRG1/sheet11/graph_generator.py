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
        print(f"Enter two numbers between 1 and {self.length} (space separated) to add a connection.")
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
                self.add_connection(input_list[0], input_list[1])


    def show_graph(self):
        print(self.graph)


    def add_connection(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def is_tree(self):
        pass

    def has_cycles(self):
        pass

    @staticmethod
    def are_connected(start, end):
        pass

g = GraphGenerator()
g.setup_vertexes()
g.setup_edges()
print(g.graph)
