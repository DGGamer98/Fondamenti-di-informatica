def calcola_area(base, altezza):
    area = base * altezza  # 'base', 'altezza' e 'area' sono nel namespace locale
    return area

calcola_area(5, 10)
# 'area' non è accessibile qui fuori