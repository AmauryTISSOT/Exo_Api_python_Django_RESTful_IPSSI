def longestPalindrome(s: str):
    print(f"Input: {s}\n")

    longest = ""

    def expandAroundCenter(left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            print(
                f"Compare s[{left}]='{s[left]}' et s[{right}]='{s[right]}' -> identiques"
            )
            left -= 1
            right += 1
        palindrome = s[left + 1 : right]
        print(f"Palindrome trouvé: '{palindrome}'")
        return palindrome

    for i in range(len(s)):
        print(f"\nCentre à l'index {i} ('{s[i]}'):")

        palindrome_odd = expandAroundCenter(i, i)
        palindrome_even = expandAroundCenter(i, i + 1)

        longest = max(longest, palindrome_odd, palindrome_even, key=len)
        print(f"Plus long palindrome trouvé actuellement: '{longest}'")

    print(f"\nRéponse finale '{longest}'")
    return longest


print(longestPalindrome("cbbd"))
