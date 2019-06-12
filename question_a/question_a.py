
def line_overlap(l1, l2):
    """
    Checks if the two lines are overlapping

    :param l1: tuple representation of line 1
    :param l2: tuple representation of line 2
    :return: Boolean depending if line2 and line 1 overlaps or not
    """
    if type(l1)!=type(l2) or type(l1)!=tuple:
        raise(ValueError("Both inputs must be tuples"))
    if len(l1)!= len(l2) or len(l2)!=2:
        raise (ValueError("Tuples must be of length 2"))
    try:
        x1 = float(min(l1))
        x2 = float(max(l1))



        x3 = float(min(l2))
        x4 = float(max(l2))
    except:
        raise ValueError("Unable to decipher some of the numbers")

    return ((x3 <= x2 <= x4) or (x3 <= x1 <= x4)) or ((x1 <= x3 <= x2) or (x1 <= x4 <= x2))