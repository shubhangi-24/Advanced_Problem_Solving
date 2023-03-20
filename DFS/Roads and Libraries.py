def roadsAndLibraries(n, c_lib, c_road, cities):
    graph=[[] for i in range(n+1)]
    for edge in cities:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    visited=[False]*(n+1)
    def dfs(u,graph,visited):
        visited[u]=True
        c=1
        for nbr in graph[u]:
            if visited[nbr]==False:
                c+=dfs(nbr,graph,visited)
        return c
    connected=[]
    for v in range(1,n+1):
        if visited[v]==False:
            comp=dfs(v,graph,visited)
            connected.append(comp)
    cost=0
    for city in connected:
        cost+=min((c_lib+(city-1)*c_road),city*c_lib)
    return cost
            
