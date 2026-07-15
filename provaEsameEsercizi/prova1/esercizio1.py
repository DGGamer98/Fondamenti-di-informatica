s = "CiaoMondo123@@"

def analisi_stringa(s):
    numeri = 0
    maiusc = 0
    min = 0
    special = 0
    
    for x in s:
        if x.isdigit():
            numeri+=1
        elif x.isupper():
            maiusc+=1
        elif x.islower():
            min+=1
            
        if not x.isalnum():
            special+=1
            
    print(f"numeri {numeri}")
    print(f"maiuscole {maiusc}")
    print(f"Minuscole {min}")
    print(f"Special {special}")
    
analisi_stringa(s)