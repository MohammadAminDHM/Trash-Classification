# Import necessary libraries
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('model\\trash_classification.h5')

# Define the classify function
def classify_image(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(384, 512))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)
    return ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash'][np.argmax(predictions)]

# Define the GUI function
def upload_image():
    file_path = filedialog.askopenfilename()
    uploaded_image = Image.open(file_path)
    uploaded_image = uploaded_image.resize((192, 256))
    uploaded_image_tk = ImageTk.PhotoImage(uploaded_image)
    label.config(image=uploaded_image_tk)
    label.image = uploaded_image_tk
    result.set("Result: " + classify_image(file_path))

# Create the GUI
root = tk.Tk()
root.title("Trash Detection")

frame = tk.Frame(root)
frame.pack(padx=100, pady=100)

label = tk.Label(frame)
label.pack(pady=20)

button = tk.Button(frame, text="Select Image", command=upload_image)
button.pack(pady=20)

result = tk.StringVar()
result.set("Result: ")
result_label = tk.Label(frame, textvariable=result)
result_label.pack(pady=20)

root.mainloop()
