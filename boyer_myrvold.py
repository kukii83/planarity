import networkx as nx
import sys

class PlanarityChecker:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edges(self, edge_list):
        """Adds a list of edges (tuples) to construct the graph."""
        self.graph.add_edges_from(edge_list)

    def test_planarity(self):
        """
        Tests whether the graph is planar using networkx planarity checking.
        """
        try:
            is_planar, embedding = nx.check_planarity(self.graph, counterexample=True)
            return is_planar, embedding
        except nx.NetworkXException as e:
            return False, str(e)


# ==========================================
# Dynamic Input Handling & Execution
# ==========================================
if __name__ == "__main__":
    print("=" * 50)
    print("Interactive Boyer-Myrvold Planarity Checker")
    print("=" * 50)

    checker = PlanarityChecker()

    print("\n[Instructions]")
    print("First, enter the number of vertices and edges (e.g., 4 6).")
    print("Then, enter each edge on a new line (e.g., 0 1).\n")

    edge_list = []
    num_vertices = 0
    num_edges = 0
    reading_header = True

    while True:
        try:
            user_input = input().strip()
        except EOFError:
            break

        if not user_input:
            continue

        parts = user_input.split()

        if reading_header:
            if len(parts) == 2:
                try:
                    num_vertices = int(parts[0])
                    num_edges = int(parts[1])
                    reading_header = False
                except ValueError as e:
                    print(f"[Error] Invalid input format: {e}")
                    sys.exit(1)
            continue

        # Reading the edges and handling invalid literal conversions
        if len(parts) == 2:
            try:
                u = int(parts[0])
                v = int(parts[1])
            except ValueError as e:
                print(f"[Error] Invalid input format: {e}")
                sys.exit(1)
            
            edge_list.append((u, v))

            if len(edge_list) >= num_edges:
                break

    if edge_list:
        checker.add_edges(edge_list)
        is_p, details = checker.test_planarity()

        print("\n" + "=" * 40)
        print("RESULTS")
        print("=" * 40)
        print(f"Graph Edges: {edge_list}")
        print(f"Total Vertices: {checker.graph.number_of_nodes()}")
        print(f"Total Edges: {checker.graph.number_of_edges()}")
        print(f"Planarity Status: {'PLANAR' if is_p else 'NON-PLANAR'}")
        
        if is_p:
            print("Planar Embedding (Vertex Order):", details)
        else:
            print("Obstruction detected: The graph contains a Kuratowski minor.")
        print("=" * 40)
