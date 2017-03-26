#!/usr/bin/env python
from argparse import ArgumentParser

import add_image
import facematch
import take_selfie

def get_args():
    parser = ArgumentParser(description='Call index faces')
    parser.add_argument('-l', '--username')
    parser.add_argument('-m', '--meds')
    return parser.parse_args()


def main():
	image = take_selfie.main()

	arg = get_args()

	add_image.main(image,arg.username,arg.meds)




