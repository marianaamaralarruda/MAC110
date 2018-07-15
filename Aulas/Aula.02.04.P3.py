#Problema: Dado um número n>0 verificar
#se n contém dois dígitos adjacente 
#iguais 
#Por exemplo: 1234321 resposta: não
#             1234556 resposta: sim
def main ():
    n= int(input("Digite n:"))
    tem= False
    dig_ant= n%10
    n= n//10
    while n>0: 
        dig_atual= n%10
        if dig_ant==dig_atual:
            tem= True
        dig_ant= dig_atual
        n= n//10
    if tem==True:
        print ("sim")
    else: 
        print ("não")
if __name__=="__main__":
    main ()