# Divisible and Non - Divisible sum difference
# Input: n = 10, m = 3
# Output: 19
# Explanation: In the given example:
# - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# We return 37 - 18 = 19 as the answer.

# n=5
# m=1
# lst=[]
# lst2=[]
# for i in range(1,n+1):
#     if i%m == 0:
#         lst.append(i)
#     else:
#         lst2.append(i)

# print(lst,lst2)
# div=0
# nondiv=0
# for i in lst:
#     div += i
# for i in lst2:
#     nondiv += i

# print(div,nondiv)
# print(nondiv-div)

# #-----------------------------------------------------------------------------

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# nums = [2, 7, 11, 15]
# target = 9

# def two_sum(nums, target):
#     lookup = {}
#     i = 0
#     while i < len(nums):
#         complement = target - nums[i]
#         if complement in lookup:
#             return [lookup[complement], i]
#         lookup[nums[i]] = i
#         i += 1

# result = two_sum(nums, target)
# print(result)

# ---------------------------------------------------------------- 

# def easytask(x, n, a):
#     seen = set()
#     count = 0
#     for num in a:
#         complement = x - num
#         if complement in seen:
#             count += 1
#         seen.add(num)
#     return count

# def main():
#     x = int(input())
#     n = int(input())
#     a = [int(input()) for _ in range(n)]
#     result = easytask(x, n, a)
#     print(result)

# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------------------------------------------------------------------------------------------
# from collections import deque
# from typing import List

# class Solution:
#     def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
#         def build_graph(edges):
#             n = len(edges) + 1
#             graph = [[] for _ in range(n)]
#             for u, v in edges:
#                 graph[u].append(v)
#                 graph[v].append(u)
#             return graph

#         def bfs_count_max(graph, max_dist):
#             n = len(graph)
#             result = [0] * n
#             for start in range(n):
#                 visited = [False] * n
#                 q = deque()
#                 q.append((start, 0))
#                 visited[start] = True
#                 count = 1
#                 while q:
#                     node, dist = q.popleft()
#                     if dist == max_dist:
#                         continue
#                     for neighbor in graph[node]:
#                         if not visited[neighbor]:
#                             visited[neighbor] = True
#                             q.append((neighbor, dist + 1))
#                             count += 1
#                 result[start] = count
#             return result

#         g1 = build_graph(edges1)
#         g2 = build_graph(edges2)

#         if k == 0:
#             return [1] * len(g1)

#         cnt1 = bfs_count_max(g1, k)
#         cnt2 = bfs_count_max(g2, k - 1)
#         max_cnt2 = max(cnt2)

#         return [cnt + max_cnt2 for cnt in cnt1]

# ------------------------------------------------------------------------------------------------------------
# Find Closest Node to Given Two Nodes
# class Solution:
#     def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
#         d1 = [float('inf') for _ in range(len(edges))]
#         d2 = [float('inf') for _ in range(len(edges))]
#         def bfs(st,dist):
#             visited = set([st])
#             queue = [(st,0)]
#             while queue:
#                 node,distance = queue.pop(0)
#                 dist[node] = distance
#                 if edges[node] != -1:
#                     if edges[node] not in visited:
#                         visited.add(edges[node])
#                         queue.append((edges[node],distance+1))
#         bfs(node1,d1)
#         bfs(node2,d2)
#         self.mini = float('inf')
#         final_node = -1
#         for i in range(len(d1)):
#             if max(d1[i],d2[i]) < self.mini:
#                 self.mini = max(d1[i],d2[i])
#                 final_node = i
#         return final_node

# ------------------------------------------------------------------------------------------------------------------

# from collections import deque
# from typing import List

# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#         n = len(board)
        
#         def get_position(square):
#             # Convert square number to board coordinates
#             row = (square - 1) // n
#             col = (square - 1) % n
#             if row % 2 == 1:  # Even rows (0-indexed) are right-to-left
#                 col = n - 1 - col
#             return n - 1 - row, col  # Convert to 0-indexed from bottom
        
#         visited = set()
#         queue = deque()
#         queue.append((1, 0))  # (current square, moves)
        
#         while queue:
#             square, moves = queue.popleft()
            
#             if square == n * n:
#                 return moves
                
#             if square in visited:
#                 continue
#             visited.add(square)
            
#             # Explore all possible dice rolls (1-6)
#             for i in range(1, 7):
#                 next_square = square + i
#                 if next_square > n * n:
#                     continue
                
#                 # Get the actual position on board
#                 r, c = get_position(next_square)
                
#                 # Check if there's a snake or ladder
#                 if board[r][c] != -1:
#                     next_square = board[r][c]
                
#                 if next_square not in visited:
#                     queue.append((next_square, moves + 1))
        
#         return -1

# ------------------------------------------------------------------------------

# nums=[2,2,36,5]
# val = 2
# z=[]
# for i in nums:
#     if i != val:
#         z.append(i)
# print(len(z))

# -----------------------------------------------------------------------------
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Computes C(x,2) = x*(x-1)//2, or 0 if x<2
        def C2(x: int) -> int:
            return (x * (x - 1) // 2) if x >= 2 else 0

        total = (n+2)*(n+1)//2 # Count = C(n+2, 2)
        x1 = n - limit + 1     # Count with a > limit 
        t1 = C2(x1)

        x2 = n - 2 * limit     # Count with a > limit
        t2 = C2(x2)            # and b > limit

        x3 = n - 3 * limit - 1 # Count with a > limit
        t3 = C2(x3)            # b > limit, c > limit

        # Inclusion–exclusion
        return total - 3 * t1 + 3 * t2 - t3