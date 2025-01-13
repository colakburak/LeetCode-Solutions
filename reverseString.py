def reverseString(s: list) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    length_of_s = len(s)

    for i in range(length_of_s // 2):
        tmp = s[i]

        s[i] = s[length_of_s-i-1]

        s[len(s)-i-1] = tmp

    print(s)


input = ["b", "u", "r", "a", "k"]
reverseString(input)
input2 = ["b", "u", "r", "a"]
reverseString(input2)
