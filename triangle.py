def classifyTriangle(a, b, c):

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'


    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if a == b == c:
        return 'Equilateral'
    elif a*2 + b2 == c2 or b2 + c2 == a2 or a2 + c2 == b*2:
        return 'Right'
    elif a != b and b != c and a != c:
        return 'Scalene'
    else:
        return 'Isosceles'
