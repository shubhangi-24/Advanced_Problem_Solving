def journeyToMoon(n, astronaut):
    graph=[[] for i in range(n)]
    for edge in astronaut:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    visited=[False]*n
    pairs=n*(n-1)//2
    def dfs(u,graph,visited):
        visited[u]=True
        counter=1
        for nbr in graph[u]:
            if visited[nbr]==False:
                counter+=dfs(nbr,graph,visited)
        return counter
    pair_list =[]  
    for v in range(n):
        if visited[v]==False:
            n_p=dfs(v,graph,visited)
            pairs-=n_p*(n_p-1)//2
    # ans=0
    # for i in range(len(pair_list)):
    #     for j in range(i+1,len(pair_list)):
    #         ans+=(pair_list[i]*pair_list[j])
    return pairs
            
