# -*- coding:utf-8 -*-
# 2017/6/9

template = """
rule silent_banker{0} : banker
    {{
        meta:
            description = "This is just an example"
            thread_level = 3
            in_the_wild = true

        strings:
            $a = {{6A 40 68 00 30 00 00 6A 14 8D 91}}
            $b = {{8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}}
            $c = "UVODFRYSIHLNWPEJXQZAKCBGMT"

        condition:
            $a or $b or $c
    }}
"""

result = ""
print template
number_rules = 1000
for each in xrange(number_rules):
    result += template.format(str(each))
print result