def verificar_ajuste(temperaturas):
    if not temperaturas:
        return "SEM DADOS"
    
    media = sum(temperaturas) / len(temperaturas)
    minima = min(temperaturas)
    
    if media > 30:
        return "VENTILAR"
    elif minima < 15:
        return "AQUECER"
    else:
        return "AUTOMATICO"

leituras = [25, 28, 32, 14, 22]
resultado = verificar_ajuste(leituras)
print(f"Modo de operação: {resultado}")