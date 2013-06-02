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

def inputs_test():
    from numpy import sqrt
    
    x_values = [0., 2., 100., 10000., 1.e-4]
    for x in x_values:
        print "Testing with x = %20.15e" % x
        s_actual = sqrt2(x)
        s_expected = sqrt(x)
        print "actual s = %20.15e expected s = %20.15e" % (s_actual, s_expected)
        assert abs(s_actual-s_expected) < 1e-14, "Disagree for x = %20.15e" % x
