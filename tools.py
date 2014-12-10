from pymongo import MongoClient
from igraph import Graph

mc = MongoClient()
db = mc.test


CLO_PATH_PARSE = 'answer/%s/closeness.txt'
DEG_PATH_PARSE = 'answer/%s/degree.txt'

def write_answer_into_mongo(graph_name):
    collection = db[graph_name]
    #collection.drop()
    '''graph = Graph.Read_Ncol('data/'+graph_name+'.txt', directed=False)
    graph = graph.simplify()
    degree_dict = {}

    for v in graph.vs:
        degree_dict[v['name']] = v.degree()'''

    '''with open(CLO_PATH_PARSE % graph_name) as clo:
        for line_id, line in enumerate(clo.readlines()):
            id_, clo = line.strip().split('\t')
            #c = collection.find_one({'node_id': id_})
            #if not c:
            c = {'node_id': id_, 'closeness': clo, 'order': line_id+1,
                 'degree': degree_dict[id_]}
            #else:
            #    c['closeness'] = clo
            #    c['order'] = line_id + 1
            #    c['degree'] = 0
            collection.insert(c)'''
    if graph_name == 'public':
        with open('data/public_nodes.txt') as f:
            for data in f:
                c = collection.find_one({'node_id': data.strip().split(',')[0]})
                c_ = {'attibute_1': data.strip().split(',')[1], 'attibute_2': data.strip().split(',')[2], 'attibute_3': data.strip().split(',')[3],
                 'attibute_4': data.strip().split(',')[4],'attibute_5':data.strip().split(',')[5]}
                c = dict(c,**c_)
                collection.save(c)
    '''
    graph = Graph.Read_Ncol('data/'+graph_name+'.txt', directed=False)
    graph = graph.simplify()
    for v in graph.vs:
        c = collection.find_one({'node_id': v['name']})
        if not c:
            c = {'node_id': id_, 'degree': v.degree()}
        else:
            c['degree'] = v.degree()
        collection.save(c)
    '''


if __name__ == '__main__':
    write_answer_into_mongo('public')
    '''
    import os
    graphs = os.listdir('answer')
    for g in graphs:
        write_answer_into_mongo(g)
        print "======%s has writed ======" % g
    '''
