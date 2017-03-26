#!/usr/bin/env python

from argparse import ArgumentParser
import boto3
from time import gmtime, strftime
import simplejson as json
import os

def get_client():
    client = boto3.client('rekognition')
    return client

<<<<<<< HEAD
def get_args():
    parser = ArgumentParser(description='Call index faces')
    parser.add_argument('-i', '--image')
    parser.add_argument('-c', '--collection')
    parser.add_argument('-l', '--label')
    return parser.parse_args()
=======

>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312

def init_file():
    if (not os.path.isfile('faces.txt')):
        with open('faces.txt', 'w') as init_file:
<<<<<<< HEAD
	    init_file.write('Date | Label | Collection | FaceId | ImageId\n')             

if __name__ == '__main__':
    args = get_args()
=======
	    init_file.write('Date | Label | Collection | FaceId | ImageId | Meds\n') 

def main(img_arg,username,meds):
>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312
    client = get_client()

    init_file()

<<<<<<< HEAD
    with open(args.image, 'rb') as image:
        response = client.index_faces(Image={'Bytes': image.read()}, CollectionId=args.collection, ExternalImageId=args.label, DetectionAttributes=['ALL'])

        with open('faces.txt', 'a') as file:
            current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            file.write(('%s | %s | %s | %s | %s\n') % (current, args.label, args.collection, response['FaceRecords'][0]['Face']['FaceId'], response['FaceRecords'][0]['Face']['ImageId']))
=======
    with open(img_arg, 'rb') as image:
        response = client.index_faces(Image={'Bytes': image.read()}, CollectionId='home', ExternalImageId=username, DetectionAttributes=['ALL'])

        with open('faces.txt', 'a') as file:
            current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            file.write(('%s | %s | %s | %s | %s |%s\n') % (current, username, 'home', response['FaceRecords'][0]['Face']['FaceId'], response['FaceRecords'][0]['Face']['ImageId']),meds)


if __name__ == '__main__':
    main()
>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312
