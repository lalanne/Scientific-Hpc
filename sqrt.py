"""
Module to calculate root square approximation
using Newton's method.
"""
def sqrt2(x, debug=False):
    """
    function that calculates root square approximation
    using Newton's method.
    """

    from numpy import nan
    if x==.0:
        return 0
    if x<.0:
        print " [ERROR] Please enter a valid number >= 0!"
        return nan
    assert x>0 and type(x) is float, "Unrecognized input!!!!!"

        
    s = 1.
    kmax = 100
    tolerance = 1.e-14

    for k in range(kmax):
        if debug:
            print "before iteration %d, s = %20.15f" % (k,s)
        s0 = s
        s = 0.5 * (s + x/s)
        delta = s - s0
        if abs(delta/x) < tolerance:
            break
    if debug:
        print "after %s iterations, s = %20.15f" % (k+1,s) 
    
    return s


