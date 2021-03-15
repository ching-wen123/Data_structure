#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    
    def BFS(self, s): 
        answer = []
        queue = [s]
        visited = defaultdict(list)    #visited必須先被定義，才能給值
        visited[s] = True
        #while queue is not None:
        #while queue != None:
        while queue:                #如果queue內有值
            vertex = queue.pop(0)
            answer.append(vertex)
            for i in self.graph[vertex]:
                if visited[i] is not True:   
                    visited[i] = True
                    queue.append(i)
            #print(answer)
            #print(queue)
            #print(id(queue))
        return answer
        

    def DFS(self, s):
        answer = []
        stack = [s]
        visited = defaultdict(list)    #visited必須先被定義，才能給值
        visited[s] = True
        while stack:                #如果queue內有值
            vertex = stack.pop()
            answer.append(vertex)
            for i in self.graph[vertex]:
                if visited[i] is not True:   
                    visited[i] = True
                    stack.append(i)
            #print(answer)
            #print(queue)
            #print(id(queue))
        return answer
        

#參考資料：https://www.youtube.com/watch?v=9wV1VxlfBlI
#參考資料：https://www.youtube.com/watch?v=zaBhtODEL0w