
def reducefract(n, d):
    '''Reduces fractions. n is the numerator and d the denominator.'''
    def gcd(n, d):
        while d != 0:
            t = d
            d = n % d
            n = t
        return n
    assert d != 0, "integer division by zero"
    assert isinstance(d, int), "must be int"
    assert isinstance(n, int), "must be int"
    greatest = gcd(n, d)
    n /= greatest
    d /= greatest
    return n, d


print(reducefract(10, 90))
