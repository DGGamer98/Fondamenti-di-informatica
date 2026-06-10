def moltiplicatore(moltiplicatore):
    def per_numero(numero):
        # 'moltiplicatore' fa parte del namespace enclosing
        return numero * moltiplicatore 
    return per_numero