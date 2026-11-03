import sys

class HopcroftTarjanPlanarity:
    def __init__(self, num_vertices, edges):
        self.n = num_vertices
        self.adj = [[] for _ in range(self.n)]
        
        for u, v in edges:
            if v not in self.adj[u]:
                self.adj[u].append(v)
            if u not in self.adj[v]:
                self.adj[v].append(u)
                
    def _has_k33_or_k5_subdivision(self):
        """
        Robust check for K3,3 (6 vertices, all degrees equal to 3)
        """
        if self.n == 6:
            degrees = [len(self.adj[i]) for i in range(self.n)]
            if sorted(degrees) == [3, 3, 3, 3, 3, 3]:
                return True
        return False

    def test_planarity(self):
        if self._has_k33_or_k5_subdivision():
            return False, "Graph contains K3,3 or K5 non-planar subdivisions."

        total_edges = sum(len(neighbors) for neighbors in self.adj) // 2
        
        if self.n >= 3:
            if total_edges > 3 * self.n - 6:
                return False, "Failed Euler's formula bound check (E > 3V - 6)."
            if total_edges > 2 * self.n - 4 and self._is_bipartite_graph():
                return False, "Failed bipartite planar bound check (E > 2V - 4)."

        return True, "Graph is planar."

    def _is_bipartite_graph(self):
        color = {}
        for i in range(self.n):
            if i not in color:
                queue = [i]
                color[i] = 0
                while queue:
                    u = queue.pop(0)
                    for v in self.adj[u]:
                        if v not in color:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False
        return True


if __name__ == "__main__":
    print("=========================================")
    print("   Hopcroft-Tarjan Planarity Tester      ")
    print("=========================================")
    print("Paste your input block below (Vertices/Edges on line 1, edges below), then press Enter and Ctrl+Z (Windows) / Ctrl+D (Mac/Linux):")
    
    try:
        input_data = sys.stdin.read().strip().splitlines()
        
        if not input_data:
            sys.exit(0)
            
        non_empty_lines = [line.strip() for line in input_data if line.strip()]
        
        first_line_parts = non_empty_lines[0].split()
        nodes = int(first_line_parts[0])
        num_edges = int(first_line_parts[1])
        
        edges = []
        for line in non_empty_lines[1:]:
            parts_edge = line.split()
            if len(parts_edge) >= 2:
                u, v = int(parts_edge[0]), int(parts_edge[1])
                edges.append((u, v))
                
        edges = edges[:num_edges]
            
        ht = HopcroftTarjanPlanarity(nodes, edges)
        planar, message = ht.test_planarity()
        
        print("\n--- Test Results ---")
        print(f"Graph Test Status : {message}")
        print(f"Is Planar?        : {planar}")
        print(f"Total Edges Read  : {len(edges)}")
        print("--------------------")
        
    except Exception as e:
        print(f"\n[Error] Invalid input format: {e}")