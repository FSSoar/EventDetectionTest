import zipfile
import shutil
import urllib.request
import os

print('Beginning file download with urllib2...')

images_url = 'http://eventdetection.web.illinois.edu/photos_2.zip'
labels_url = 'http://eventdetection.web.illinois.edu/labels_2.zip'
urllib.request.urlretrieve(images_url, 'photos.zip')
print('Successfully downloaded images.zip')
urllib.request.urlretrieve(labels_url, 'labels.zip')
print('Successfully downloaded labels.zip')

images = zipfile.ZipFile('photos.zip', 'r')
for files in images.namelist():
    images.extract(files, 'darknet/images')
print('Successfully extracted images.zip')
labels = zipfile.ZipFile('labels.zip', 'r')
for files in labels.namelist():
    labels.extract(files, 'darknet/images')
print('Successfully extracted labels.zip')
images.close()
labels.close()


#THIS PUTS ALL THE IMAGES AND TEXT FILES IN THE SAME FOLDER
sourceDir = 'darknet/images/labels'
destDir = 'darknet/images/'
files = os.listdir(sourceDir)
for f in files:
    try:
        sourceFile = os.path.join(sourceDir, f)
        directoryFile = os.path.join(destDir, f)
        shutil.move(sourceFile, destDir)
    except:
        pass
sourceDir = 'darknet/images/photos'
files = os.listdir(sourceDir)
for f in files:
    try:
        sourceFile = os.path.join(sourceDir, f)
        directoryFile = os.path.join(destDir, f)
        shutil.move(sourceFile, destDir)
    except:
        pass

if not os.path.isdir('darknet/labels'):
    os.makedirs('darknet/labels')
sourceDir = 'darknet/images'
destDir = 'darknet/labels'
files = os.listdir(sourceDir)
for f in files:
    if f[-4:] != ".txt":
        continue
    try:
        sourceFile = os.path.join(sourceDir, f)
        directoryFile = os.path.join(destDir, f)
        shutil.copy(sourceFile, destDir)
    except:
        pass

os.remove("images.zip")
os.remove("labels.zip")
shutil.rmtree("darknet/images/photos")
shutil.rmtree("darknet/images/labels")

print("files deleted")

