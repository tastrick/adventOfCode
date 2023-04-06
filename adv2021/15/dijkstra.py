from Graph import Graph
import sys
class dijkstra:
    def __init__(self,graph,nodes,start_node,end_node):
        self.graph = Graph(nodes,graph)
        self.start_node = start_node
        self.target = end_node
        p,s = self.algorithm()
        print(s)
        #self.print_result(p,s)
        #print('ran algorithm')
    def algorithm(self):
        unvisited_nodes = list(self.graph.get_nodes())
        shortest_path = {}
        previous_nodes = {}
        max_value =sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[self.start_node]=0
        cnt = 0
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node]<shortest_path[current_min_node]:
                    current_min_node = node
            neighbors = self.graph.get_outgoing_edges(current_min_node)
            for n in neighbors:
                tentative_value = shortest_path[current_min_node]+self.graph.value(current_min_node,n)
                if (tentative_value<shortest_path[n]):
                    shortest_path[n] = tentative_value
                    previous_nodes[n] = current_min_node
            unvisited_nodes.remove(current_min_node)
            cnt+=1
            if (cnt%100000==0):
                print(i,len(unvisited_nodes))
        return previous_nodes,shortest_path

    def print_result(self,previous_nodes, shortest_path):
        path = []
        node = self.target
        
        while node != self.start_node:
            path.append(node)
            node = previous_nodes[node]
    
        # Add the start node manually
        path.append(self.start_node)
        
        print("We found the following best path with a value of {}.".format(shortest_path[self.target]))
        print(" -> ".join(reversed(path)))


    
