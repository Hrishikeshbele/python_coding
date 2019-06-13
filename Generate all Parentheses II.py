'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.
 n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"

'''



class Solution:
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, n):
	    #list to store pair of paratheses
        res = []
        #using stack and itialising stack with intial values of x,l,r
        #x-curr pair of pars,l-opening bracket,r-closing bracket
        s = [("(", 1, 0)]
        #run loop until stack is not empty
        while s:
            #assigning value to x,l,r every iteration
            x, l, r = s.pop()
            #if curr pair is not valid then moving to next pair
            if l - r < 0 or l > n or r > n:
                continue
            #when we reach to condition where l=r=n i.e no of closing 
            #and opening bracket are equal then that is valid str and append that to res
            if l == n and r == n:
                res.append(x)
            #for every pair add opening parth and increase l and wise-versa
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        #since we have to return sorted string
        return res[::-1]

#2nd elegent solution

class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        result = []
	#using helper function to find all pairs
        def helper(left, right, soFar):
	#left-no of opening parth,right-closing parth
	#unvalid conditions
            if left < 0 or right < 0 or left > right:
                return
	#no opening and closing bracket left
            if left == right == 0:
                result.append(soFar)
                return
	#adding opening parth and decreasing left count by 1 and vice-versa
            helper(left-1, right, soFar + '(')
            helper(left, right-1, soFar + ')')
        
        helper(A, A, '')
        return result
