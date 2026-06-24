def function (s):
    counter = 0
    for x in s:
        if x.isdigit(s):
            counter+=1
        elif x.isaplha(s):
            counter+=1
    return counter