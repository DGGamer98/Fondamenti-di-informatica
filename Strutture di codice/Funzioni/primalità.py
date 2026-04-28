def is_primo(n):
    '''Ritorna True se n è primo altrimenti False'''
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0 :
            return False
        
    return True

print(is_primo(347))