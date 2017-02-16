import sys


t = int(raw_input().strip())
values = list()
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    
    for v in a:
        if v <= 0:
            k-=1
    
    if k > 0:
        print "YES"
    else:
        print "NO"
