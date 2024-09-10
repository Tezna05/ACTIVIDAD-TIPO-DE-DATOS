#DEFINIMOS UNA VARIABLE DE TIPO FLOTANTE
saldo=100.0
#SIMULAMOS UN CICLO DE RETIROS DE SALDO SEA MENOR DE 10
while saldo > 10:
    retiro = 15.0
    saldo-=retiro
    print(f"se ha retirado{retiro}, saldo actual:{saldo}")
