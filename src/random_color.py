#!/usr/bin/env python3
'''
A thin wrapper around randomcolor.RandomColor.generate()

USAGE:
    (base) [twesleyb@archos]$ ./random_color.py -c 3
                              ['#4039d3', '#e86a92', '#e83f33']

    In [0]: import random_color

    In [1]: random_color.random_color()
    Out[1]: ['#0dad38']

    In [1]: print(random_color.random_color(3))
    Out[1]: ['#d657c5', '#c6a200', '#bf7bd8']

    In [1]: print(random_color.random_color(count=6, hue = 'bright'))
    Out[1]: ['#9843bc', '#f1b4f7', '#3ed673', '#f262f7', '#3dd138', '#8bb227']
'''

## imports

import argparse
import randomcolor

## functions

def rmNone(args):
    ''' remove None type items from a dictionary '''
    rm = [key for key in args if args.get(key) is None]
    for key in rm: del args[key]
    return args
#EOF


def parse_arguments():
    '''
    parse input arguments with argparse parse_args
    '''
    #NOTE: randomcolors's seed argument doesn't seem to work.
    #ap.add_argument('-s','--seed', type = int,
    #default=None, help=''' ''')
    ap = argparse.ArgumentParser('''
            generate a random color''')
    ap.add_argument(
        '-c',
        '--count',
        default = 1,
        type = int,
        help='''An integer specifying the number of
        colors to generate.
        ''')
    ap.add_argument(
        '-u',
        '--hue',
        type = str,
        default=None,
        help='''
        Controls the hue of the generated color.
        You can pass a string representing a color name:
        red, orange, yellow, green, blue, purple,
        pink and monochrome are currently supported.
        ''')
    ap.add_argument(
        '-l',
        '--luminosity',
        type = str,
        default=None,
        help='''
        Controls the luminosity of the generated color.
        You can specify a string containing bright,
        light, or dark.
        ''')
    ap.add_argument(
        '-f',
        '--format',
        type = str,
        default=None,
        help='''
        A string which specifies the format of the
        generated color. Possible values are rgb,
        rgbArray, hsl, hslArray and hex (default).
        ''')
    # parse command line input and remove None
    args = rmNone(vars(ap.parse_args()))
    return args
#EOF


def random_color(count=1,hue=None,
        luminosity=None,format=None):
    args = rmNone(locals())
    rand_color = randomcolor.RandomColor()
    return rand_color.generate(**args)
#EOF

## main

if __name__ == "__main__":

    args = parse_arguments()

    print(random_color(**args))
