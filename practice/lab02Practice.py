from collections import deque


def is_balanced_parentheses(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def next_greater_to_right(nums: list[int]) -> list[int]:
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result


def first_non_repeating(stream: str) -> str:
    q = deque()
    count = {}
    result = ""

    for ch in stream:
        count[ch] = count.get(ch, 0) + 1
        q.append(ch)

        while q and count[q[0]] > 1:
            q.popleft()

        if q:
            result += q[0]
        else:
            result += '#'

    return result


def hot_potato(names: list[str], k: int) -> str:
    q = deque(names)

    while len(q) > 1:
        for _ in range(k):
            q.append(q.popleft())

        q.popleft()

    return q[0]


# -------------------------
# Practice Testing (Printing Results)
# -------------------------

print("Q1 Balanced Parentheses")
print(is_balanced_parentheses("([]){}"))
print(is_balanced_parentheses("(]"))
print(is_balanced_parentheses("a+(b*c)-{d/e}"))

print("\nQ2 Next Greater Element")
print(next_greater_to_right([2,1,2,4,3]))

print("\nQ3 First Non Repeating Character")
print(first_non_repeating("aabc"))

print("\nQ4 Hot Potato")
print(hot_potato(["A","B","C","D"],2))
