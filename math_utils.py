# Intencionalmente vacío o sin la función 'es_par' para provocar RED.

# print("Ingrese un numero:")
# n = 0
# input(n)

def es_par(n) -> bool:
    
    mod = n % 2

    if mod == 0:
        return True 
    else:
        return False
