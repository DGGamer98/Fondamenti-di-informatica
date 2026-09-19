'''Metdodo readline()'''
# with open("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/isolamisteriosa.txt", "r",) as s:
#     file = s.readline()

#     counter = 0

#     for x in file:
#         counter+=1
#         print(f"{counter}: {file}")

'''Metodo readlines()'''
with open ("/home/dgatta/Desktop/Fondamenti-di-informatica/Gestione dei file/apertura e chiusura/isolamisteriosa.txt", "r",) as s:
    lines = s.readlines()
    #lines = s.readline()
    #print(lines)
    for line in lines:
        print(line)