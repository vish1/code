#!/usr/bin/python

def check_uniq_string(inp_str):
    inp_str = inp_str.lower()
    return "Yes" if len(set(inp_str)) == len(inp_str) else "No"

if __name__ == "__main__":
    print check_uniq_string("aaaaa")
    print check_uniq_string("")
    print check_uniq_string("a")
    print check_uniq_string("abc")
    print check_uniq_string("bababa")
