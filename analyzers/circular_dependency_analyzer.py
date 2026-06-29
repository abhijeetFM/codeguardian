class CircularDependencyAnalyzer:

    def __init__(self):

        self.graph = {}

    def build_graph(self, dependencies):

        for dep in dependencies:

            source = dep.source_file
            target = dep.target_module

            if source not in self.graph:
                self.graph[source] = []

            self.graph[source].append(target)

    def dfs(
        self,
        node,
        visited,
        rec_stack
    ):

        visited.add(node)
        rec_stack.add(node)

        for neighbor in self.graph.get(node, []):

            if neighbor not in visited:

                if self.dfs(
                    neighbor,
                    visited,
                    rec_stack
                ):
                    return True

            elif neighbor in rec_stack:

                return True

        rec_stack.remove(node)

        return False

    def detect(self, dependencies):

        self.build_graph(dependencies)

        visited = set()
        rec_stack = set()

        for node in self.graph:

            if node not in visited:

                if self.dfs(
                    node,
                    visited,
                    rec_stack
                ):
                    return True

        return False