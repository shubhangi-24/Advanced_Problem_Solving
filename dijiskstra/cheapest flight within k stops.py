class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def build_graph(flights):
            graph=[]
            for i in range(n):
                graph.append(list())
            for flight in flights:
                graph[flight[0]].append((flight[1],flight[2]))
            return graph

        graph=build_graph(flights)
        min_heap=[]
        distance=[math.inf]*(n+1)
        stops=[math.inf]*(n+1)

        distance[src]=0
        stops[src]=0
        heappush(min_heap,(0,0,src))
        while min_heap:
            cur_dist,cur_stop,cur_node=heappop(min_heap)

            if cur_node==dst:
                return cur_dist
            if cur_stop==k+1:
                continue
            for nbr,dist in graph[cur_node]:
                new_dist=cur_dist+dist
                new_stop=cur_stop+1
                if new_dist<distance[nbr]:
                    distance[nbr]=new_dist
                    stops[nbr]=new_stop
                    heappush(min_heap,(new_dist,new_stop,nbr))
                elif new_stop<stops[nbr]:
                    heappush(min_heap,(new_dist,new_stop,nbr))

        return -1
