#!/usr/bin/env python

import boto3 as b3
from argparse import ArgumentParser
from time import gmtime, strftime
 
def get_client():
    return b3.client('rekognition')

<<<<<<< HEAD
def get_args():
    parser = ArgumentParser(description='Compare an image')
    parser.add_argument('-i', '--image')
    parser.add_argument('-c', '--collection')
    return parser.parse_args()
=======
>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312

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

<<<<<<< HEAD
def main():
    args = get_args()
=======
def main(img_arg):
>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312
    
    client = get_client()
    
    print '[+] Running face checks against image...'
<<<<<<< HEAD
    result, resp = check_face(client, args.image)
=======
    result, resp = check_face(client, img_arg)
>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312

    if (result):
        print '[+] Face(s) detected with %r confidence...' % (round(resp['FaceDetails'][0]['Confidence'], 2))
        print '[+] Checking for a face match...'
<<<<<<< HEAD
        resu, res = check_matches(client, args.image, args.collection)
    
        if (resu):
            print '[+] Identity matched %s with %r similarity and %r confidence...' % (res['FaceMatches'][0]['Face']['ExternalImageId'], round(res['FaceMatches'][0]['Similarity'], 1), round(res['FaceMatches'][0]['Face']['Confidence'], 2))
=======
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
                            

>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312
        else:
            print '[-] No face matches detected...' 

    else :
        print "[-] No faces detected..."
<<<<<<< HEAD
        
if __name__ == '__main__':
    main()
=======



        
if __name__ == '__main__':
    main()
>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312
