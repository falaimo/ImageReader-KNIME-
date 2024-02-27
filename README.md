# ImageReader-KNIME-
Una soluzione in python per KNIME che rimpiazza i nodi Image reader, Image Calculator e Image Resizer

Questa soluzione utilizza Python e le librerie PyTorch per creare un nodo in Python, da includere in un workflow di **KNIME Analytics Platform**, che sostituisca i nodi Imager Reader, Image Calculator e Image Resize.
Questo è stato necessario per sopperire ad una limitazione dei nodi indicati che, se utilizzati per elaborare una mole consistente di immagini, manifestano tempi di elaborazione lunghissimi e, quello che è peggio, un utilizzo di spazio sul disco, in termini di files temporanei creati da KNIME, che può saturare la disponibilità della propria macchina, con conseguente arresto del workflow.
La soluzione trovata, sicuramente perfettibile, permette di superare i problemi sopra indicati.
Richiede un **env** creato ad hoc, per implementare le librerie **pytorch**.
Per creare l'env è necessario eseguire i seguenti steps:
- creare l'env: **conda create --name pytorch python=3.8**
- attivarlo: **conda activate pytorch**
- installare i pacchetti necessari: **conda install -c pytorch torchvision pandas cudatoolkit**
Le cudatoolkit sono necessarie se si ha una GPU nvida e la si vuole utilizzare (sempre che l'hardware sia supportato)
