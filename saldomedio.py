saldo = float (input ("Informe o valor do seu saldo médio:"))

if saldo<500 : print ("Não há limite.")
if saldo<=0 : print ("Não foi possivel concluir o valor.")
if saldo>=500 and saldo<1000 : print ("limite:" , saldo*0.08)
if saldo>=1000 : print ("limite:" , saldo*0.15)
    

