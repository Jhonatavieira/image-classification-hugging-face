from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests
import torch
import matplotlib.pyplot as plt 

# Load the feature extractor for the vision transformer 
feature_extractor =  ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')

# Load the pre-trained weights from vision transformer 
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

# Read the image from the workspace using the matplotlib library 
image = plt.imread('laptop.jpeg')

# Display image 
plt.imshow(image)

# Extract the features from the image using the feature extractor 
inputs = feature_extractor(images=image, return_tensors='pt')

# Extract pixel values from the image 
pixel_values = inputs['pixel_values']

# Make predictions using the model
outputs = model(pixel_values)

# Get the logits (raw scores) for differente classes
logits = outputs.logits

# Determine the number of classes in the model
# print(logits.shape)

# Find the index of class with the highest score
predicted_class_idx = logits.argmax(-1).item()

# Extract the class name from the model's configuration
predicted_class = model.config.id2label[predicted_class_idx]

print(predicted_class)