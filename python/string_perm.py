#!/usr/bin/python

def perm_strings(str1, str2):
    if len(str1) != len(str2):
        return "No"
    if set(str1) - set(str2):
        return "No"
    return "Yes"

if __name__ == "__main__":
    print perm_strings("aaa", "aa")
    print perm_strings("aba", "ab")
    print perm_strings("abc", "cba")
