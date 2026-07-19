# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# train_path = "dataset/train"
# test_path = "dataset/test"

# train_data = ImageDataGenerator(rescale=1./255)
# test_data = ImageDataGenerator(rescale=1./255)

# # train = train_data.flow_from_directory(
# #     directory=train_path,
# #     target_size=(150, 150),
# #     batch_size=32,
# #     class_mode='binary'
# # )

# # test = test_data.flow_from_directory(
# #     directory=test_path,
# #     target_size=(150, 150),
# #     batch_size=32,
# #     class_mode='binary'
# # )

# # print(train.class_indices)

# # import tensorflow as tf
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from tensorflow.keras.models import Sequential
# # from tensorflow.keras.layers import Conv2D,Maxpooling2D,Flatten,Dense
# # from tensorflow.keras.preprocessing import image
# # model = Sequential()
# # model.add(Conv2D(
# #     filters =32,
# #     kernal_size = (3,3),
# #     activation = 'relu',
# #     input_shape = (150,150,3)
# # ))


 
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
 
# # load dataset
# train_data = ImageDataGenerator(rescale=1./255)
# test_data = ImageDataGenerator(rescale=1./255)
 
# train = train_data.flow_from_directory(
#     train_path,
#     target_size=(150, 150),
#     batch_size=32,
#     class_mode='binary'
# )
 
# test = test_data.flow_from_directory(
#     test_path,
#     target_size=(150, 150),
#     batch_size=32,
#     class_mode='binary'
# )
 
# print("train data index")
# print(train.class_indices)
 
# print("test data index")
# print(test.class_indices)
 
# # model
# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt
 
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
# from tensorflow.keras.preprocessing import image
 
# # model
 
# model = Sequential()
 
# # first convolution layer
# model.add(Conv2D(
#     filters=32,
#     kernel_size=(3,3),
#     activation='relu',
#     input_shape=(150,150,3)
# ))
 
# # first pooling layer
# model.add(MaxPooling2D(pool_size=(2,2)))
 
# # second convolution layer
# model.add(Conv2D(
#     filters=64,
#     kernel_size=(3,3),
#     activation='relu'
# ))
 
# # second pooling layer
# model.add(MaxPooling2D(pool_size=(2,2)))
 
# # third convolution layer
# model.add(Conv2D(
#     filters=128,
#     kernel_size=(3,3),
#     activation='relu'
# ))
 
# # third pooling layer
# model.add(MaxPooling2D(pool_size=(2,2)))
 
# # Flatten layer
# model.add(Flatten())
 
# # hidden layer
# model.add(Dense(units=128,activation='relu'))
 
# #output layer
# model.add(Dense(units=1,activation='sigmoid'))
 
# # model summary
# print(model.summary())

# # compille
# model.compile(optimizer = 'adam',loss = 'binary_crossentropy',metrics = ['accuracy'])

# history = model.fit(train,validation_data = test,epochs=10)

# model.save("dog_cat_classifier.keras")


# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image

# model = load_model("dog_cat_classifier.keras")

# img = image.load_img("image1.jpeg",target_size=(150,150))

# img_array = image.img_to_array(img)

# img_array = img_array/255.0

# img_array = np.expand_dims(img_array,axis=0)

# # prediction
# pred = model.predict(img_array)
# # print(pred)

# if pred[0][0] > 0.5:
#   print("Dog")
# else:
#   print("cat")
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing import image

# ===========================
# DATASET PATH
# ===========================

# Option 1 (Recommended): Full path
train_path = r"C:\Users\Dell_owner\Desktop\dataset\train"
test_path = r"C:\Users\Dell_owner\Desktop\dataset\test"

# Option 2 (Use only if dataset folder is in the same folder as CNN.py)
# train_path = "dataset/train"
# test_path = "dataset/test"

# ===========================
# CHECK PATH
# ===========================

print("Current Working Directory:", os.getcwd())
print("Train Folder Exists:", os.path.exists(train_path))
print("Test Folder Exists:", os.path.exists(test_path))

if not os.path.exists(train_path):
    raise FileNotFoundError(f"Train folder not found:\n{train_path}")

if not os.path.exists(test_path):
    raise FileNotFoundError(f"Test folder not found:\n{test_path}")

# ===========================
# IMAGE GENERATOR
# ===========================

train_data = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_data = ImageDataGenerator(rescale=1./255)

# ===========================
# LOAD DATA
# ===========================

train = train_data.flow_from_directory(
    directory=train_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

test = test_data.flow_from_directory(
    directory=test_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

print("\nClass Indices:")
print(train.class_indices)

# ===========================
# CNN MODEL
# ===========================

model = Sequential()

model.add(Conv2D(
    filters=32,
    kernel_size=(3,3),
    activation='relu',
    input_shape=(150,150,3)
))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(
    filters=64,
    kernel_size=(3,3),
    activation='relu'
))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(
    filters=128,
    kernel_size=(3,3),
    activation='relu'
))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))

model.add(Dense(1, activation='sigmoid'))

model.summary()

# ===========================
# COMPILE MODEL
# ===========================

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ===========================
# TRAIN MODEL
# ===========================

history = model.fit(
    train,
    validation_data=test,
    epochs=10
)

# ===========================
# SAVE MODEL
# ===========================

model.save("dog_cat_classifier.keras")

print("\nModel Saved Successfully!")

# ===========================
# LOAD MODEL
# ===========================

model = load_model("dog_cat_classifier.keras")

# ===========================
# TEST IMAGE
# ===========================

img_path = "image1.jpeg"

if os.path.exists(img_path):

    img = image.load_img(img_path, target_size=(150,150))

    img_array = image.img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    print("Prediction Value:", prediction)

    if prediction[0][0] > 0.5:
        print("Prediction: Dog 🐶")
    else:
        print("Prediction: Cat 🐱")

else:
    print(f"\nTest image '{img_path}' not found.")