import pytest
from src.palindrome_finder import find_palindrome_substrings

def test_palindrome_basic():
    """Test basic palindrome substring finding"""
    assert find_palindrome_substrings("aabaa") == ['aabaa', 'aba', 'aa', 'aa']

def test_palindrome_no_palindromes():
    """Test string with no palindromes"""
    assert find_palindrome_substrings("abcde") == ['a', 'b', 'c', 'd', 'e']

def test_palindrome_empty_string():
    """Test empty string"""
    assert find_palindrome_substrings("") == []

def test_palindrome_single_char():
    """Test single character string"""
    assert find_palindrome_substrings("a") == ['a']

def test_palindrome_multiple_same_length():
    """Test palindromes of same length"""
    assert find_palindrome_substrings("racecar") == ['racecar', 'aceca', 'cec', 'aa', 'r', 'a', 'c', 'e']

def test_palindrome_complex_example():
    """Test a more complex example"""
    result = find_palindrome_substrings("babadada")
    expected = ['adada', 'ada', 'ada', 'aa', 'babab', 'bab', 'aa', 
                'a', 'b', 'a', 'd']
    assert result == expected

def test_palindrome_sorting():
    """Verify sorting by length and then alphabetically"""
    result = find_palindrome_substrings("banana")
    # Expected to have sorted palindromes
    expected = ['anana', 'ana', 'ana', 'aa', 'a', 'a', 'a', 'b', 'n']
    assert result == expected