from collections import defaultdict
import sys

def search_winners(graph, n):
    if not graph[n][0]:
        return graph

    for i in graph[n][0].copy():
        graph[n][0].update(graph[i][0])
    return search_winners(graph, i)
    
def search_losers(graph, n):
    if not graph[n][1]:
        return graph

    for i in graph[n][1].copy():
        graph[n][1].update(graph[i][1])
    return search_losers(graph, i)

def solution(n, results):

    graph = defaultdict(lambda : (set(), set()))
    answer = 0        ##########  win   lose
    for i in results: # ex) {1 : (2,3), (5), 2 : (5, 6), (1), ...}
        graph[i[0]][1].add(i[1])
        graph[i[1]][0].add(i[0])

    for i in graph.copy():
        for _ in range(n+1):
            graph = search_winners(graph, i)
            graph = search_losers(graph, i)
    
    for val in graph.values():
        if len(val[0]) + len(val[1])  == n - 1:
            answer += 1 
            
    return answer