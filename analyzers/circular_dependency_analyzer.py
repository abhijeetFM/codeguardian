
class CircularViolation:

    def __init__(self, cycle):

        self.cycle = cycle


class CircularDependencyAnalyzer:

    def __init__(self):

        self.graph = {}

    def build_graph(self, dependencies):

        self.graph = {}

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
        rec_stack,
        path,
        cycles
    ):

        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        for neighbor in self.graph.get(node, []):

            if neighbor not in visited:

                self.dfs(
                    neighbor,
                    visited,
                    rec_stack,
                    path,
                    cycles
                )

            elif neighbor in rec_stack:

                cycle_start = path.index(
                    neighbor
                )

                cycle = (
                    path[cycle_start:]
                    + [neighbor]
                )

                cycle_tuple = tuple(cycle)

                if cycle_tuple not in {

                    tuple(c)

                    for c in cycles
                }:

                    cycles.append(cycle)
        rec_stack.remove(node)
        path.pop()

    def detect(self, dependencies):

        self.build_graph(dependencies)

        visited = set()
        rec_stack = set()
        cycles = []

        for node in self.graph:

            if node not in visited:

                self.dfs(
                    node,
                    visited,
                    rec_stack,
                    [],
                    cycles
                )

        return [
            CircularViolation(cycle)
            for cycle in cycles
        ]