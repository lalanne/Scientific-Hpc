"""
module to calculate root square.
"""
def sqrt2(x):
    s = 1.
    kmax = 100
    tolerance = 1.e-14

    for k in range(kmax):
        print "before iteration %d, s = %20.15f" % (k,s)
        s0 = s;
        s = 0.5 * (s + x/s)
        delta = s - s0
        if abs(delta/x) < tolerance:
            break
    print "after %s iterations, s = %20.15f" % (k+1,s) 



