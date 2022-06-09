import sys
sys.stdin=open("input.txt","r") #파일 입출력을 위한
def DFS(x):
    if x>0:
        DFS(x-1)
        print(x, end=' ')

if __name__=="__main__":
    n=int(input())
    DFS(n)