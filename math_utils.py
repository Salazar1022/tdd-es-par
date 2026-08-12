# Intencionalmente vacío o sin la función 'es_par' para provocar RED.

def es_par(n) -> bool:
    
    mod = n % 2

    if mod == 0:
        return True 
    else:
        return False

def es_multiplo_de(n, m) -> bool:

    if m == 0: 
        return False
        
    mul = n % m

    if mul == 0:
        return True
    else:
        return False
