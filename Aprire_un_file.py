# Come l'ho fatto io:
# with open("isolamisteriosa.txt","rt") as f:
#     counter = 0
#     for i in f:
#         counter += 1
#         i = f.readline()
#         print (counter, i,"\n")

# Come l'ha fatto il prof:
with open("isolamisteriosa.txt","rt") as f:
    counter = 0
    for i in f:
        counter += 1
        print (f"{counter}: {i}")