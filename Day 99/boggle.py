from collections import deque
class Solution:
    def wordBoggle(self,g,d):
        r=len(g)
        c=len(g[0])
        dx=[-1,-1,-1,0,0,1,1,1]
        dy=[-1,0,1,-1,1,-1,0,1]
                
        def isSafe(x,y):
            return x>=0 and y>=0 and x<r and y<c
        def bfs(x,y,k,s):
            q=deque()
            n=len(s)
            q.append((x,y,k))
            vis=[[False for _ in range(c)] for _ in range(r)]
        
            vis[x][y]=True
            while(q):
                i,j,k=q.popleft()
                k+=1
                
                if(k>=n):
                    return True
                for z in range(8):
                    x=i+dx[z]
                    y=j+dy[z]
                    if(isSafe(x,y) and vis[x][y]==False and k<n and g[x][y]==s[k]):
                        q.append((x,y,k))
                        vis[x][y]=True
                    
            return False
        def dfs(x,y,level,s):
            n=len(s)
            if(level==n):
                return True
            if(not isSafe(x,y)):
                return False
            if(g[x][y]==s[level]):
                t=g[x][y]
                g[x][y]="#"
                res=dfs(x-1,y,level+1,s) or dfs(x+1,y,level+1,s) or dfs(x,y-1,level+1,s) or dfs(x,y+1,level+1,s) or dfs(x-1,y+1,level+1,s) or dfs(x+1,y+1,level+1,s) or dfs(x+1,y-1,level+1,s) or dfs(x-1,y-1,level+1,s)
                g[x][y]=t
                return res
            else:
                return False
        ans=[]
        d1={}
        for k in d:
            d1[k]=False
        def check(k):
            
            for i in range(r):
                for j in range(c):
                    if(g[i][j]==k[0]):
                        if(dfs(i,j,0,k)):
                            return True
    
        for k in d:
            if(check(k) == True):
                ans.append(k)
                
        ans.sort()
        return ans
