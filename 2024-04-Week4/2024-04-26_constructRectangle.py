"""
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

"""
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        Max_L = 0
        Min_W = area
        
        for L in range(1, area+1):
            if area % L != 0:
                continue
            else:
                Max_L = max(Max_L, L)
                Min_W = min(Min_W, int(area/Max_L))
        
                if Max_L >= Min_W:
                    break
        return [Max_L, Min_W]