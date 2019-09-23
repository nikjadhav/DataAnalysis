'''
PROBLEM STATEMENT:https://www.hackerrank.com/challenges/crush/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    wf={}
    wf=dict.fromkeys(strings,0)
    res=[]
    for i in strings:
        wf[i]=wf[i]+1
    for i in queries:
        try:
            res.append(wf[i])
        
        except:
            res.append(0)
    return res

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    
    res = matchingStrings(strings, queries)
    print(res)
    matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
