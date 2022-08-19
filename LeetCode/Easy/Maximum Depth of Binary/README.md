# 🔔 LeetCode - Level: Easy

## 📑 Maximum Depth of Binary
### 📌 문제 설명
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
### ✔ 제한 사항
- The number of nodes in the tree is in the range [0, 104].
- -100 <= Node.val <= 100
### 💡 아이디어
dfs 깊이 탐색으로 해당 노드의 왼쪽 오른쪽에 노드가 있는지 확인하고 있다면 다음 깊이 노드를 다시 탐색한다. 
노드가 없다면 현재 깊이를 리턴한다. 
왼쪽 오른쪽 중에 깊이가 깊은 것을 리턴한다. 

### 💬 개선사항

