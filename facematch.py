#!/usr/bin/env python

import boto3 as b3
from argparse import ArgumentParser
from time import gmtime, strftime
 
def get_client():
    return b3.client('rekognition')


def check_face(client, file):
    face_detected = False
    with open(file, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()})
        if (not response['FaceDetails']):
            face_detected = False
        else: 
            face_detected = True

    return face_detected, response

def check_matches(client, file, collection):
    face_matches = False
    with open(file, 'rb') as image:
        response = client.search_faces_by_image(CollectionId=collection, Image={'Bytes': image.read()}, MaxFaces=1, FaceMatchThreshold=85)
        if (not response['FaceMatches']):
            face_matches = False
        else:
            face_matches = True

    return face_matches, response

def main(img_arg):
    
    client = get_client()
    
    print '[+] Running face checks against image...'
    result, resp = check_face(client, img_arg)

    if (result):
        print '[+] Face(s) detected with %r confidence...' % (round(resp['FaceDetails'][0]['Confidence'], 2))
        print '[+] Checking for a face match...'
        resu, res = check_matches(client, img_arg, 'home')
    
        if (resu):
            print '[+] Identity matched %s with %r similarity and %r confidence...' % (res['FaceMatches'][0]['Face']['ExternalImageId'], round(res['FaceMatches'][0]['Similarity'], 1), round(res['FaceMatches'][0]['Face']['Confidence'], 2))

            with open('faces.txt', 'a') as file:
                data = file.read().split
                i =0
                for word in data:
                    i++
                    if word == res['FaceMatches'][0]['Face']['ExternalImageId']:
                        med = data[i+4]
                        if med == 'tictac':
                            print tictac
                            break
                        elif med == 'skittle':
                            print skittle
                            break
                        else:
                            print mikenike
                            break
                            

        else:
            print '[-] No face matches detected...' 

    else :
        print "[-] No faces detected..."



        
if __name__ == '__main__':
    main()