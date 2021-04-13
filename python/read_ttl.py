import re
from collections import namedtuple
from itertools import takewhile
from SPARQLWrapper import SPARQLWrapper, JSON
from py2neo import Graph, Node, Relationship

Entry = namedtuple('Entry', '疾病 症状')


def get_entries(path):
    with open(path) as file:
        i = 1
        for line in file.readlines():
            print(line)
            i += 1
            if i > 100:
                break


def select():
    sparql = SPARQLWrapper("http://localhost:3030/test/sparql")
    sparql.setQuery("""
        SELECT ?subject ?predicate ?object
        WHERE {
            ?subject ?predicate ?object
        }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # for result in results["results"]["bindings"]:
    #     print(result["subject"]["value"], end='\t')
    #     print(result['predicate']['value'], end='\t')
    #     print(result['object']['value'])

    test_graph = Graph(
        "http://localhost:7474",
        username="neo4j",
        password="969696"
    )
    node_dic = set()
    for result in results["results"]["bindings"]:
        na = result["subject"]["value"]
        if '#' in na:
            na = na.split('#')[-1]
        elif '/' in na:
            na = na.split('/')[-1]
        node_dic.add(na)
        na = result["object"]["value"]
        if '#' in na:
            na = na.split('#')[-1]
        elif '/' in na:
            na = na.split('/')[-1]
        node_dic.add(na)

    n = 1
    for i in node_dic:
        node = Node(name=i)
        test_graph.create(node)
        print(f'------实体： {n} ------')
        n += 1

    n = 1
    for result in results["results"]["bindings"]:
        n1 = result["subject"]["value"]
        n2 = result["object"]["value"]

        na = result["predicate"]["value"]
        if '#' in na:
            na = na.split('#')[-1]
        elif '/' in na:
            na = na.split('/')[-1]

        query = "match p,q where p.name='%s'and q.name='%s' create (p)-[rel:{name:'%s'}]->(q)" % (
            n1, n2, na)
        test_graph.run(query)
        print(f'------关系： {n} ------')
        n += 1


def main():
    # get_entries('/Users/admin/Downloads/nlp/nlp.ttl')
    select()


if __name__ == '__main__':
    main()
