#!/usr/bin/env python

from argparse import ArgumentParser
import boto3
from time import gmtime, strftime
import simplejson as json
import os

def get_client():
    client = boto3.client('rekognition')
    return client



def init_file():
    if (not os.path.isfile('faces.txt')):
        with open('faces.txt', 'w') as init_file:
	    init_file.write('Date | Label | Collection | FaceId | ImageId | Meds\n') 

def main(img_arg,username,meds):
    client = get_client()

    init_file()

    with open(img_arg, 'rb') as image:
        response = client.index_faces(Image={'Bytes': image.read()}, CollectionId='home', ExternalImageId=username, DetectionAttributes=['ALL'])

        with open('faces.txt', 'a') as file:
            current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            file.write(('%s | %s | %s | %s | %s |%s\n') % (current, username, 'home', response['FaceRecords'][0]['Face']['FaceId'], response['FaceRecords'][0]['Face']['ImageId']),meds)


if __name__ == '__main__':
    main()