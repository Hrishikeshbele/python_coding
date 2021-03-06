'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that 
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container
contains the most water.
Note: You may not slant the container and n is at least 2.

the idea here is to use 2 pointers and move the left pointer and right pointer respectively to search for the next higher height.If height[L] < height[R],
move toward right(increment left pointer), else move left since Say height[0] < height[5],since area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than 
(0, 5) since height will be equal to height[0] and lenth would const decrease, so no need to try them.           
ex.
[3....<10 sticks>....5]` water between 3, 5 = 3*11 = 33.
Argument: You have to move 3 because moving the index at 5 will certainly reduce the water level.
        3...<10 sticks>....8,5 => Water is 3*10 = 30 which is lower than before.
        i                  j
        3...<10 sticks>....2,5 => Again lower in this case as compared to the maximal
        
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0
        end=len(height)-1
        area=[]
        
        while start<end:
            if height[start]<=height[end]:
                #area = length * min (height_a, height_b), to maximize the area we want max both lenght and height
                area.append(min(height[end],height[start])*(end-start))
                start+=1   
                
            else:
                area.append(min(height[end],height[start])*(end-start))
                end-=1
                
            
                  
            
        return max(area)
            
            
