# import pyrebase

# config = {
#   'apiKey': "AIzaSyBPOepsepxQ-4Qy3m8Cu-UJJbK3pxGIw5c",
#   'authDomain': "testuploadfile-9d666.firebaseapp.com",
#   'projectId': "testuploadfile-9d666",
#   'storageBucket': "testuploadfile-9d666.appspot.com",
#   'messagingSenderId': "89611931041",
#   'appId': "1:89611931041:web:b5e7460379e45e07a54fe0",
#   'serviceAccount' : "serviceAccount.json",
#   'databaseURL' : "gs://testuploadfile-9d666.appspot.com"
# }

# firebase = pyrebase.initialize_app(config)
# storage = firebase.storage()
# storage.child("4NDVI.jpg").put('4_NDVI.jpg')

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate('testuploadfile-9d666-firebase-adminsdk-iomvc-28668e19a4.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'testuploadfile-9d666.appspot.com'
})

def upload_image(file_path, destination_path):
    bucket = storage.bucket()
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)

upload_image('4_NDVI.jpg', '4_NDVI.jpg')

# def download_image(source_path, destination_path):
#     bucket = storage.bucket()
#     blob = bucket.blob(source_path)
#     blob.download_to_filename(destination_path)

# download_image('4_NDVI.jpg', 'dataRead/4_NDVI.jpg')

def list_all_items():
    bucket = storage.bucket()
    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)

list_all_items()