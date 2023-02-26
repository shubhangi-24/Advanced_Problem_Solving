class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_graph(v,edges):
            graph=[]
            indegree={}
            for i in range(v):
                graph.append(list())
                indegree[i]=0
            for edge in edges:
                graph[edge[0]].append(edge[1])
                indegree[edge[1]]+=1
            return graph,indegree

        graph,indegree=build_graph(numCourses,prerequisites)
        queue=deque()
        for key,value in indegree.items():
            if value==0:
                queue.append(key)

        order=[]
        while queue:
            cur_node=queue.popleft()
            order.append(cur_node)

            for nbr in graph[cur_node]:
                indegree[nbr]-=1
                if indegree[nbr]==0:
                    queue.append(nbr)

        if len(order)==numCourses:
            return True
        else:
            return False
        
