import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Creiamo il contenitore vuoto
model = models.Sequential(name="Rete_Immobiliare_v1")

# 2. Aggiungiamo il PRIMO Hidden Layer
# È fondamentale specificare input_shape SOLO qui.
# 32 neuroni, attivazione ReLU per la non-linearità.
model.add(layers.Dense(32, activation='relu', input_shape=(10,), name="Hidden_Layer_1"))

# 3. Aggiungiamo un SECONDO Hidden Layer
# Nota: Keras capisce da solo che l'input di questo strato
# è l'output di quello precedente (32). Non serve più input_shape.
model.add(layers.Dense(16, activation='relu', name="Hidden_Layer_2"))

# 4. Aggiungiamo l'OUTPUT Layer
# 1 solo neurone perché vogliamo un solo numero (prezzo).
# Nessuna attivazione ('linear') perché il prezzo può essere qualsiasi numero.
model.add(layers.Dense(1, activation='linear', name="Output_Layer"))

model.summary()