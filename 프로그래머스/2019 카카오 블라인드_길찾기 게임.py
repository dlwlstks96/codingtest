# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6) #재귀 호출 제한 해제

class Node:
    def __init__(self, key, x):
        self.key = key
        self.x = x
        self.right, self.left = None, None
    
class Tree:
    def __init__(self, head, x):
        self.head = Node(head, x)
        
    def insert(self, key, x):
        cur_node = self.head
        while True: #루트 노드부터 단말 노드 위치까지 내려감
            if cur_node.x > x: #left down
                if cur_node.left == None: #None일때만 노드 insert
                    cur_node.left = Node(key, x)
                    break
                else: cur_node = cur_node.left #cur_node 갱신
            elif cur_node.x < x: #right down
                if cur_node.right==None: 
                    cur_node.right = Node(key, x)
                    break
                else: cur_node = cur_node.right

    #전위 순회 / 부모 -> 왼쪽 자식 -> 오른쪽 자식
    def preorder(self):
        res = []  
        def order(node):
            nonlocal res
            res.append(node.key)
            if node.left != None: order(node.left)
            if node.right != None: order(node.right)
        order(self.head)
        return res
        
    #후위 순회 / 왼쪽 자식 -> 오른쪽 자식 -> 부모
    def postorder(self):
        res = []
        def order(node):
            nonlocal res
            if node.left != None: order(node.left)
            if node.right != None: order(node.right)
            res.append(node.key)
        order(self.head)
        return res
        
def solution(nodeinfo):
    answer = []
    
    #인덱스 정보 저장
    for i in range(len(nodeinfo)):
        nodeinfo[i] = [i+1] + nodeinfo[i]      
        
    #y값 기준으로 내림차순 정렬
    nodeinfo.sort(key=lambda x:(x[2]), reverse=True)
    
    #Tree와 함께 루트 노드까지 생성
    tree = Tree(nodeinfo[0][0], nodeinfo[0][1])
    
    #모든 노드를 트리에 삽입
    for i in nodeinfo[1:]:
        tree.insert(i[0], i[1])    
    
    answer.append(tree.preorder())
    answer.append(tree.postorder())
    
    return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])