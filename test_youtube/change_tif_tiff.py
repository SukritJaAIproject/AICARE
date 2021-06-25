import os
folder_path = ('/content/drive/MyDrive/AIHealthcare/AIcare_Phrase1/data/trainset/surprise/')
test = os.listdir(folder_path)
for images in tqdm(test):
    if images.endswith(".tif"):
        os.remove(os.path.join(folder_path, images))

folder_path = ('/content/drive/MyDrive/AIHealthcare/AIcare_Phrase1/data/trainset/surprise/')
test = os.listdir(folder_path)
for images in tqdm(test):
    if images.endswith(".tiff"):
        os.remove(os.path.join(folder_path, images))