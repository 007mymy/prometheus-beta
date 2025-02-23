def find_palindrome_substrings(s: str) -> list:
    """
    Find all palindrome substrings in a given string.
    
    Args:
        s (str): Input string to search for palindrome substrings
    
    Returns:
        list: Sorted list of palindrome substrings, 
              sorted first by length (descending), 
              then alphabetically
    
    Examples:
        >>> find_palindrome_substrings("aabaa")
        ['aabaa', 'aba', 'aa', 'aa']
        >>> find_palindrome_substrings("abcde")
        ['a', 'b', 'c', 'd', 'e']
    """
    # Handle edge cases
    if not s or len(s) == 0:
        return []
    
    # List to store palindrome substrings
    palindromes = []
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.append(substring)
    
    # Sort palindromes by length (descending) and then alphabetically
    # Use sorted with a custom key that ensures exact sorting requirements
    return sorted(
        palindromes, 
        key=lambda x: (-len(x), x), 
        reverse=False
    )