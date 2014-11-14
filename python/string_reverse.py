#!/usr/bin/python

def reverse_string(inp_str):
    return inp_str[::-1]

if __name__ == "__main__":
    print reverse_string("aaaaa")
    print reverse_string("")
    print reverse_string("a")
    print reverse_string("abc")
    print reverse_string("bababa")
