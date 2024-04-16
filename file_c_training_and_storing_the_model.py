from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import json
from keras import models, layers, losses
import seaborn as sns

# Initialize the number of rows, columns, and iterations
dim_row = 27
dim_col = 19
iters = 10

# Open the file that is used to train and test the model
with open(f"json_files/gesturespersons1-20WOhitting_pokeEmptiesRemoved..json", 'r') as file:
    data = json.load(file)

# Save the frame data to the X_data
X_data = np.array([d["frame"] for d in data])
# Save the label to the y_data with help of the dictionary
dict_key = {'regular': 0, 'petting': 1, 'poking': 2, 'comforting': 3, 'scratching': 4}
y_data = np.array([dict_key[d["label"]] for d in data])

# Split all data in training and testing data #0.25 #0.2
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.25)
# Split the training data in training and validation data #0.2 #0.1
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2)

# Set the batch size
batch_size = 16


# Drop the remainder of data so all batches are full
def drop_remain(X,y):
    # Calculate the remainder
    remain = X.__len__() % batch_size
    # If there is no remainder, pass the x and y data back
    if remain == 0:
        return X, y
    # If there is a remainder, remove it
    else:
        X = X[:-remain, :,:]
        y = y[:-remain]
        return X, y

# Remove the remainder for all data
X_train, y_train = drop_remain(X_train, y_train)
X_test, y_test = drop_remain(X_test, y_test)
X_val, y_val = drop_remain(X_val, y_val)

#newmodel734_704_1-14
#Mo_B16_741_700_1-14
#Mo_B16_712_706_1-14.h5
#MO_B16_781_761_1-14WOH  <--------------------------------------------

# Create the LSTM model with 3 hidden layers
model = models.Sequential()
model.add(layers.LSTM(128, stateful=True, return_sequences=True))
model.add(layers.LSTM(128, stateful=True, return_sequences=True))
model.add(layers.LSTM(128, stateful=True))
model.add(layers.Dense(5))



'''model = models.Sequential()
model.add(layers.LSTM(64, stateful=True, return_sequences=True))
model.add(layers.LSTM(64, stateful=True, return_sequences=True))
model.add(layers.LSTM(64, stateful=True))
model.add(layers.Dense(6))'''

'''model = models.Sequential()
model.add(layers.LSTM(32, stateful=True, return_sequences=True))
model.add(layers.LSTM(32, stateful=True, return_sequences=True))
model.add(layers.LSTM(32, stateful=True, return_sequences=True))
model.add(layers.Dense(6))'''


# Compile the model
model.compile(optimizer='adam',
              loss=losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Fit the model and save the data for the plots
#hist = {'loss':[],'accuracy':[]} # When not using validation data
hist = {'loss':[],'accuracy':[],'val_loss':[],'val_accuracy':[]} # When using validation data
for i in range(iters):
    #epoch_hist = model.fit(X_train,y_train, epochs=1, batch_size=batch_size, verbose=2, shuffle=False) # When not using validation data
    epoch_hist = model.fit(X_train, y_train, validation_data=(X_val, y_val),
                           epochs=1, batch_size=batch_size, verbose=2, shuffle=False) # When using validation data

    # Store the data in hist under the appropriate key
    for key in hist.keys():
        hist[key].append(epoch_hist.history[key])

    # Reset the states in the LSTM layers
    for layer in model.layers:
        if layer.name == 'lstm':
            layer.reset_states()

# Make a graph that plots the accuracy against epochs
plt.plot(hist['accuracy'], label='accuracy')
plt.plot(hist['val_accuracy'], label = 'val_accuracy') # When using validation data
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

# Save the model so it can be accessed later
model.save('MO_test.h5')

# Calculate the loss and accuracy with the test data and print this
test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2, batch_size=batch_size)
print(test_loss, test_acc)

# Create the confusion matrix with the test data
y_pred = model.predict(X_test, batch_size=batch_size)
y_pred = np.argmax(y_pred, axis=1)
conf_matrix = confusion_matrix(y_test, y_pred)
# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title('Confusion Matrix for Decision Tree')
plt.show()



