import json


def  getData(data,r):

    if ('[' in r):
        #si esta out of bounds mostrar toda la lista
        if (int(r[r.index('[')+1:r.index(']')]) > len(data.get(r[:r.index('[')]))):
            return(data.get(r[:r.index('[')]))
        #si no, mostrar el indice especificado    
        else:
            #si tiene, un '.', es una lista de dict. 
            if('.' in r):
                #lo que esta despues del punto es el campo del dict.
                return(data.get(r[:r.index('[')])[int(r[r.index('[')+1:r.index(']')])].get(r[r.index('.')+1:]))
            else:
                #no hay punto, tonces mostramos la lista en el indice, que a esta altura no esta out of bounds
                return(data.get(r[:r.index('[')])[int(r[r.index('[')+1:r.index(']')])])

    else:
        if('.' in r):
            return(data.get(r[:r.index('.')]).get(r[r.index('.')+1:]))
        else:
            return(data.get(r))

################################################################


f = open('data.json')
data = json.load(f)

r = 'contactDetails.phone'
print(getData(data,r))
r = 'friends[5].name'
print(getData(data,r))
r = 'friends[1].name'
print(getData(data,r))
r = 'contactDetails'
print(getData(data,r))

f.close()








