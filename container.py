"""
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.
"""

def maxArea(height):
    most_water = 0
    i = 0
    j = len(height) - 1

    while j-i > 0:
        temporal_square = min(height[i], height[j]) * (j-i)

        if temporal_square > most_water:
            most_water = temporal_square

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return most_water
