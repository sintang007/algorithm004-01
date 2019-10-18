# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足： 
#
# 
# 左括号必须用相同类型的右括号闭合。 
# 左括号必须以正确的顺序闭合。 
# 
#
# 注意空字符串可被认为是有效字符串。 
#
# 示例 1: 
#
# 输入: "()"
# 输出: true
# 
#
# 示例 2: 
#
# 输入: "()[]{}"
# 输出: true
# 
#
# 示例 3: 
#
# 输入: "(]"
# 输出: false
# 
#
# 示例 4: 
#
# 输入: "([)]"
# 输出: false
# 
#
# 示例 5: 
#
# 输入: "{[]}"
# 输出: true
# Related Topics 栈 字符串

"""
1 replace 替换解法
2 stack解法
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

    def isValid1(self, s):
        if len(s) & 1 == 1:  # 位运算判断奇偶
            return False

        while len(s):
            tmp = s
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
            if s == tmp:
                return False
        return True

    def isValid2(self, s):
        if len(s) & 1 == 1:  # 位运算判断奇偶
            return False

        stack = []
        hash_map = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in hash_map:
                top_element = stack.pop() if stack else '#'
                if hash_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

# leetcode submit region end(Prohibit modification and deletion)
