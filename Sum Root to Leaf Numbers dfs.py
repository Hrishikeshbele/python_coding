'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.

we find elms in each path and then make int out of them and add them to get final no to devide by 10003.

'''

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        ans=[]
        def helper(A,curr):
            if not A:
                return 
            if not A.left and not A.right:
                ans.append(int(''.join(curr+[str(A.val)])))
                return 
            helper(A.left,curr+[str(A.val)])
            helper(A.right,curr+[str(A.val)])
        helper(A,[])
        
        return sum(ans)%1003
