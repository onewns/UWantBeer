import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from datetime import timedelta

cred = credentials.Certificate('beer/fireauth.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'u-on-beer.appspot.com'
})

bucket = storage.bucket()
# print(bucket.name)
# print(bucket.list_blobs())
# print(bucket.get_blob('cass.jpg'))
# for blob in bucket.list_blobs():
#     print(blob.name)
#     print(blob.generate_signed_url(expiration=100, version="v4"))

def getURL(beer_name:str):
    image = bucket.get_blob(beer_name)
    if image:
        url = image.generate_signed_url(expiration=timedelta(minutes=1), version="v4")
        return url
    else:
        return None




