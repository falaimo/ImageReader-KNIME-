#la tabella in ingresso contiene quattro campi con questi nomi/tipo:
#Path/Path: percorso del file nel sistema operativo in uso
#Location/String: uguale a Path ma in formato String
#Class/String: classe associata all'immagine
#cracked/Integer: uguale a Class ma ricavata con una regola (il risultato è 0 o 1)

import os
import pandas as pd
import torch
from torchvision import transforms
from PIL import Image

# Verifica la disponibilità della GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Carica e elabora le immagini sulla GPU se presente
elaborate_images = []
for img_path in input_table_1['Location']:
    img = Image.open(img_path).convert('RGB')

    # Normalizza i colori nell'immagine
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0, 0, 0), (1, 1, 1))  # Divide automaticamente per 255
    ])
    img = transform(img).to(device)

    # Riduci le dimensioni dell'immagine
    resized_img = transforms.functional.resize(img, (64, 64)).to(device)  # Specifica le dimensioni desiderate

    # Aggiungi l'immagine elaborata alla lista
    elaborate_images.append(resized_img)

#crea una collection dai valori dei tensori
tensor_list=[]
i=0
for ts in elaborate_images:
	collection=ts.flatten().tolist()
	tensor_list.append(collection)
	i=i+1
  #mostra a video un messaggio con il numero attuale di immagine convertita
	print("Elaborata immagine ",i)

#salva il dataframe con le colonne che mi servono
output_table_1 = pd.DataFrame({'Location':input_table_1['Location'],'Immagini':tensor_list,'Class':input_table_1['Class'],'Cracked':input_table_1['cracked']})
