def length_of_longest_substring(s):
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


def largest_rectangle_area(heights):
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

def my_sqrt( x):
    """
    :type x: int
    :rtype: int
    """
    min_num = 0
    max_num = x
    while min_num <= max_num:
        mid = (min_num + max_num) // 2
        if mid * mid < x:
            min_num = mid + 1
        elif mid * mid > x:
            max_num = mid - 1
        else:
            return mid
    return max_num

print(largest_rectangle_area([0, 9, 9]))