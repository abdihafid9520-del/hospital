def average(a,b,c,d,e):
    average_grade=a+b+c+d+e
    return average_grade
def grade(average_grade):
    total=average_grade/5
    return total
def score(total):
    if total>=80:
        return "A"
    elif total>=75:
        return"A-"
    elif total>=70:
        return"B+"
    elif total>=65:
        return"B"
    elif total>=60:
        return"B-"
    elif total>=55:
        return"C+"
    elif total>=50:
        return"fail"
    return score


