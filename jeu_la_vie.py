import numpy as np
from matplotlib import pyplot as plt

frame =  np.array([[0,0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]])

#ici on a calculé le nombre des voisins (la fonction me donne un entier qui représente le nombre des voisins)
def compute_number_neighbors(paded_frame,index_line,index_column):
  neighbors=0
  for i in range(index_line-1,index_line+2):
    for j in range(index_column-1,index_column+2):
      if i!=index_line or j!=index_column:
        neighbors+=paded_frame[i][j]
  return neighbors
#on veut parcourir la matrice paded_frame mais je veux savoir les elements de la matrice avant l'ajout des zeros(avant de la rendre comme paded frame)
def compute_next_frame(frame):
  paded_frame=np.pad(frame,1,mode='constant')
  for u in range(1,len(paded_frame)-1):
    for v in range(1,len(paded_frame[0])-1):
      voisins=compute_number_neighbors(paded_frame,u,v)
#la fonction compute number neighbors me donne le nombre des voisins seulement
      i=u-1
      j=v-1
      if frame[i][j]==0 and voisins==3:
        frame[i][j]=1
      elif frame[i][j]==1 and (voisins<2 or voisins>3):
        frame[i][j]=0

  return frame
while True:
    #Calculer la prochaine variation de matrice avec les régles de la jeu de la vie
    frame=compute_next_frame(frame)
    #Afficher la matrice dans une interface graphique
    plt.imshow(frame, interpolation='nearest')
    #Figer le graphe pendant 3 secondes
    plt.pause(3)