# Definisci una funzione : ListDif che prende in input due liste , l1 e l2 e ritorna una lista che è la differeza delle liste l1 e l2 . Utilizza i parametri di default , dove l2 è un parametro = [1,2,3,4,5] in modo tale che la nostra ListDif possa essere chiamata con un solo parametro oppure con 2 parametri. 

def ListDif ( l1, l2 = [1,2,3,4,5] ):

    diff = [x for x in l2 if not x in l1]
    
    print(diff)

a = [1,2,3,4,5]
b = [3,6,7]

ListDif(b) 