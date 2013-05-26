
x = 9.
s = 1.

for k in range(6):
    print "before iteration %s, s = %s" % (k,s)
    s = 0.5 * (s + x/s)

print "after %s iterationsi, s = %s" % (k+1,s) 
