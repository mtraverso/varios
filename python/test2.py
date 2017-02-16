def sum(arr):
    sum = 0
    for x in xrange(0,len(arr)):
        sum+=int(arr[x])
    return sum

def printArr (arr):
    val = ""
    for x in arr:
        val+= x+" "
    return val 

testCases = 1
for test in xrange(0,int(testCases)):
    nstr,kstr = "6 2".split(' ')
    arr = "1 2 1 2 1 2".split(' ')
    print arr
    qty = 0
    
    n = int(nstr)
    t = n
    k = int(kstr)
    for i in xrange(0,int(n)):
        for j in xrange(0,n-t+1):
            val = sum(arr[j:j+t]) 
            if val % k == 0:
                qty += 1
        t-=1
                
    print qty

