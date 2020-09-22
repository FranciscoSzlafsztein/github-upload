#%%
#Voy a estudiar la migracion de un grupo de aves 
import os
os.chdir('C:\\Users\\Francisco-pc\\Desktop\\Facultad\\Python edX\\Week 4') #Me ubico en la cartpeta donde tengo la informacion

import pandas as pd
birddata = pd.read_csv("bird_tracking.csv")   #Cargo mi data

birddata.info()   #Veo que tengo de informacion


#Veamos el recorrido de una sola ave
import matplotlib.pyplot as plt
import numpy as np

ix = birddata.bird_name == 'Eric'    #Me creo una variable que solo contenga la informacion asociada al nombre 'Eric'
x , y =  birddata.longitude[ix] , birddata.latitude[ix] #Creo un par ('touple') de variables que corresponde a los datos sobre la longitud y latitud de Eric

plt.figure(figsize=(7,7))    #Ploteo la posicion de Eric
plt.plot(x,y,'.')

#Ahora veamos esto para las 3 aves:
bird_names = pd.unique(birddata.bird_name) #Creo un array con los valores de birddata.bird_name sin repetir (Los nombres de las aves)

plt.figure(figsize=(7,7))    #Creo una figura
for bird_name in bird_names:                #Voy a iterar para c/ave
    ix = birddata.bird_name == bird_name    #Me creo una variable que solo contenga la informacion asociada a un ave
    x , y =  birddata.longitude[ix] , birddata.latitude[ix] #Creo un par ('touple') de variables que corresponde a los datos sobre la longitud y latitud del ave
    plt.plot(x,y,'.',label=bird_name)                      #Ploteo la hubicacion del ave.
plt.xlabel("Logitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")





#Ahora voy a ahcer un histograma con las velocidades de Eric
ix = birddata.bird_name == 'Eric'    #Me creo una variable que solo contenga la informacion asociada al nombre 'Eric'
speed = birddata.speed_2d[ix]  #Me creo una serie con los valores de la velocidad en 2D de Eric
ind = np.isnan(speed)       #Creo una lista de los indices de la lista 'speed' que tienen valores que no son numericos, estos traerian problemas al tratar de hacer el histograma con nunpy (con pandas no son problema)
plt.hist(speed[~ind], bins=np.linspace(0,30,20), normed=True)    #Creo el histograma de las velocidades excluyendo los indices que no son numericos ('ind' contiene 'True' si el valor NO es un numero y 'False' si es un numero. Por otro lado '~' me cambia un bool 'True' por un 'False' y viceversa,
                                                                # por lo que al indicar que el histograma use los indices de speed correspondiente a '~ind', estoy tomando solo los indices correspondientes a numeros, ignorando los 'NaN' ('not a number')), el histograma está normalizado con 'normed=True'
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frecuency")

#Este ploteo con pandas seira asi (aqui no nos importa los NaNs porque pandas se ocupa solo de ellos):
birddata.speed_2d.plot(kind='hist', range=[0,30])
plt.xlabel("2D speed")








