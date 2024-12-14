def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    saved_chars = {}
    max_length = 0
    for i in range(len(s)):
        saved_chars[i] = {}
        curr_length = 0
        for char in s[i:]:
            if len(saved_chars[i]) == 0 or char not in saved_chars[i]:
                saved_chars[i][char] = 0
                curr_length += 1
            else:
                if curr_length > max_length:
                    max_length = curr_length
                break
            if curr_length > max_length:
                max_length = curr_length
    return max_length


def largestRectangleArea( heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    heights.pop()
    return ans


print(largestRectangleArea([0,9,9]))