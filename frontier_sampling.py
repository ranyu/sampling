from igraph import *
from random import sample,random,choice
from core import Algorithm
from egraphs import FBEgoGraph

class MDRandomWalk(Algorithm):

    def update_graph(self, start_node, new_node):
        g = self.sampled_graph
        start_id = g.vs['name'].index(start_node)
        if new_node['name'] not in g.vs['name']:
            g.add_vertex(**new_node)
            index = g.vs['name'].index(new_node['name'])
            g.add_edge(start_id,index)
        else:
            index = g.vs['name'].index(new_node['name'])
            if g.get_eid(start_id, index, directed=False, error=False) == -1:
                g.add_edge(start_id,index)


    def run(self,k,m = 5):
        degree_sum = 0
        node_set = sample(self.sampled_graph.vs['name'],m)
        for sv in node_set:
            degree_sum += self.sampled_graph.degree(sv)

        n_attribute = len(self.sampled_graph.vertex_attributes())-2
        i = 0

        while i < k:
            for j in xrange(len(node_set)):
                if j == len(node_set)- 1:
                    start_node = node_set[-1]
                    break
                else:
                    ra = random()
                    if ra >= self.sampled_graph.degree(str(node_set[j]))/degree_sum and ra < self.sampled_graph.degree(str(node_set[j+1]))/degree_sum:
                        start_node = node_set[j]
                        break
            query_result = self.egraph.query_node(start_node,n_attribute)
            for nd in query_result:
                if nd['name'] in self.sampled_graph.vs['name']:
                    self.update_graph(start_node,nd)
            new_node = choice(query_result)
            self.update_graph(start_node,new_node)
            i += 1

if __name__ == "__main__":
    fbego_graph = FBEgoGraph('data/egofb.txt')
    fuck_mdrw = MDRandomWalk(fbego_graph)
    print fuck_mdrw.validate()
