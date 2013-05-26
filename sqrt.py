
x = 10000.
s = 1.
kmax = 100
tolerance = 1.e-14

for k in range(kmax):
    print "before iteration %s, s = %s" % (k,s)
    s0 = s;
    s = 0.5 * (s + x/s)
    delta = s - s0
    if abs(delta/x) < tolerance:
        break

print "after %s iterations, s = %s" % (k+1,s) 



