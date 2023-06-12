# Scrivere un programma che crea una lista che contiene solo i numeri pari tra 10 e 25 , per fare questo bisogna usare un for loop che utilizza un range tra 10 e 30 ,e all' interno di questo loop scartare i numeri dispari qundi considerare solo i numeri pari e minori di 25 , per aggiungere alla lista i numeri utilizza il metodo append().

# myList  = [] 
# for i in range(10 , 30) :
#     if i % 2 == 0 and i < 25 :   
#         myList.append(i)
#         print (myList)

# ora applica una list comprehension

l= [n for n in range(10 , 30) if n % 2 == 0 and n < 25]
print (l)