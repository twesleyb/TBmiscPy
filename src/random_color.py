#!/usr/bin/env python3
'''
A thin wrapper around randomcolor.RandomColor.generate()
'''

#NOTE: randomcolors's seed argument doesn't seem to work.
#ap.add_argument('-s','--seed', type = int,
#default=None, help=''' ''')

## imports ----------------------------------------------

import argparse
import randomcolor

## functions ---------------------------------------------

def rmNone(args):
    ''' remove None type items from a dictionary '''
    rm = [key for key in args if args.get(key) is None]
    for key in rm: del args[key]
    return args


def parse_arguments():
    '''
    parse input arguments with argparse parse_args
    '''
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
    # parse input and remove None
    args = rmNone(vars(ap.parse_args()))
    return args


def random_color(count=1,hue=None,
        luminosity=None,format=None):

    args = parse_arguments()

    # init rand_color
    rand_color = randomcolor.RandomColor()

    # generate colors
    print(rand_color.generate(**args))


## main --------------------------------------------------

if __name__ == "__main__":
    random_color()
#EOF
