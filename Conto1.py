# Definisci la classe ContoCorrente
class ContoCorrente:
    
    def __init__(self, nome , conto, importo):
        self.nome = str(nome)
        self.conto = int(conto)
        self.__saldo = int(importo)
        
 
    def preleva(self , importo):
        importo = int(input("Inserisci l'importo da prelevare: \n"))
        self.__saldo -= importo 
        
    def deposita(self , importo):
        importo = int(input("Inserisci l'importo da depositare: \n"))
        self.__saldo += importo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,importo):
        self.preleva(self.__saldo)
        self.deposita(importo)
        
    def descrizione (self):
        print("Intestatario:{}".format(self.nome) + "\n" ,"N.conto:{}".format(self.conto)+"\n" ,"Saldo Totale:{}".format(self.__saldo) + "\n")

myContoCorrente1 = ContoCorrente("Domenico Caraviello", 78662448521 , 300.00)
myContoCorrente1.preleva(0)
myContoCorrente1.descrizione()
myContoCorrente1.deposita(0)
myContoCorrente1.descrizione()
        
