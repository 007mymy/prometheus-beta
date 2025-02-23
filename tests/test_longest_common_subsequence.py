import pytest
from src.longest_common_subsequence import find_longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenario"""
    assert find_longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert find_longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when strings are identical"""
    test_str = "hello world"
    assert find_longest_common_subsequence(test_str, test_str) == test_str

def test_no_common_subsequence():
    """Test when no common subsequence exists"""
    assert find_longest_common_subsequence("abc", "xyz") == ""

def test_empty_strings():
    """Test with empty strings"""
    assert find_longest_common_subsequence("", "") == ""
    assert find_longest_common_subsequence("abc", "") == ""
    assert find_longest_common_subsequence("", "xyz") == ""

def test_partial_match():
    """Test scenarios with partial matches"""
    assert find_longest_common_subsequence("abcde", "ace") == "ace"
    assert find_longest_common_subsequence("programming", "program") == "program"

def test_type_error():
    """Test type checking"""
    with pytest.raises(TypeError):
        find_longest_common_subsequence(123, "abc")
    with pytest.raises(TypeError):
        find_longest_common_subsequence("abc", None)
    with pytest.raises(TypeError):
        find_longest_common_subsequence([], "abc")

def test_case_sensitivity():
    """Test case sensitivity in different contexts"""
    # Different cases should not match
    assert find_longest_common_subsequence("Hello", "hello") == ""
    assert find_longest_common_subsequence("AbCdEf", "aBcDeF") == ""
    
    # Case-sensitive matches
    assert find_longest_common_subsequence("HeLLo", "Hello") == ""
    assert find_longest_common_subsequence("HeLLo", "HeLXo") == "HeL"