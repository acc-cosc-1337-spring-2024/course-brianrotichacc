
def get_students_who_took_prog1_and_prog2(prog1, prog2):
    result  = prog1.intersection(prog2)
    return result

def get_students_who_took_prog1_not_prog2(prog1, prog2):
    result = prog1.difference(prog2)
    return result

def get_students_who_took_prog1_or_prog2(prog1, prog2):
    result = prog1.union(prog2)
    return result   


def get_students_who_took_prog2_not_prog1(prog1, prog2):
    result = prog2.difference(prog1)
    return result

