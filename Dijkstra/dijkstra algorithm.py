import math
from heapq import *
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        min_heap=[]
        distance=[math.inf]*V
        visited=[False]*V
        distance[S]=0
        heappush(min_heap,(distance[S],S))
        while min_heap:
            cur_dist,cur_node=heappop(min_heap)
            if visited[cur_node]:
                continue
            visited[cur_node]=True
            for nbr in adj[cur_node]:
                if visited[nbr[0]]:
                    continue
                if cur_dist+nbr[1]<distance[nbr[0]]:
                    distance[nbr[0]]=cur_dist+nbr[1]
                    heappush(min_heap,(distance[nbr[0]],nbr[0]))
                    
        return distance
