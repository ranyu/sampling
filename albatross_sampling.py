from igraph import *
from random import sample,random,choice
from core import Algorithm
from egraphs import FBEgoGraph

class AlbatrossSampling(Algorithm):

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


    def run(self,k,p_jump=0.02):
        start_node = choice(self.sampled_graph.vs['name'])
        n_attribute = len(self.sampled_graph.vertex_attributes())-2
        i = 0

        while i < k:
            query_result = self.egraph.query_node(start_node,n_attribute)
            for nd in query_result:
                if nd['name'] in self.sampled_graph.vs['name']:
                    self.update_graph(start_node,nd)
            new_node = choice(query_result)
            self.update_graph(start_node,new_node)
            if random() < p_jump:
                start_node = choice(self.sampled_graph.vs['name'])
            elif random() < float(self.sampled_graph.degree(start_node))/self.sampled_graph.degree(new_node['name']):
                start_node = new_node['name']
            i += 1

if __name__ == "__main__":
    fbego_graph = FBEgoGraph('data/egofb.txt')
    fuck_as = AlbatrossSampling(fbego_graph)
    print fuck_as.validate()
