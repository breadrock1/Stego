#!/usr/bin/python3

"""
    Copyright 2021 Bread White

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Author: Bread White
    Date:   2021 year
    Email: breadrock1@gmail.com
"""

from argparse import ArgumentParser, Namespace, ArgumentError
from logging import warning, exception, info
from pathlib import Path

from stego.decoder import Decoder
from stego.encoder import Encoder


DEFAULT_KEYS_PATH = Path(__file__) / 'keys.txt'


def inject_message(args: Namespace):
    output_file = Encoder().inject_message(
        image_file_path=args.f,
        keys_file_path=args.o,
        message=args.m
    )

    info(msg=f'The target file with message is: {output_file}')
    info(msg=f'The key file with private code is: {args.o}')
    info(msg=f'The process has been done successful!')


def extract_message(args: Namespace):
    extracted_message = Decoder().extract_message(
        image_file_path=args.f,
        keys_file_path=args.k
    )

    info(msg=f'The extracted message is: {extracted_message}')
    info(msg=f'The process has been done successful!')


def main(args: Namespace):
    try:
        inject_message(args) if args.mode is "inject" else extract_message(args)

    except ArgumentError as err:
        exception(msg=f'Failed while parsing passed arguments: {err}.')
        argumentParser.print_usage()

    except Exception as err:
        exception(msg=f'Unknown runtime exception: {err}.')
        warning(msg='Please check usage and try again!')
        argumentParser.print_usage()


if __name__ == "__main__":
    argumentParser = ArgumentParser(
        prog='Stego',
        usage='''python3 stego.py { inject [options] | extract [options] } -f <picture-file-path>
                    There are two modes to use this simple application:
                    1. inject  - Allows to inject passed string message to stego-container. There are 
                                 following additional needed options: 
                                        -m <message-string> [-o <output-key-file-path>]
                    
                    2. extract - Allows to extract string message from stego-container. Just pass key 
                                 file path: -k <key-file-path>

                    For mode details for each other modes enter '--help'.
                ''',
        description='''
                    There is simple python script that i had been implemented while studying at the University.
                    The main goal of current project was being familiarization with python programming language.
                    And i decided to implement this simple python script that provides ability to inject/extract
                    passed string message to/from PNG image stego-container. So you're welcome! :)
                ''',
        add_help=True,
        allow_abbrev=True
    )

    subArgumentParser = argumentParser.add_subparsers(title='Script Mods', dest='mode')
    inject = subArgumentParser.add_parser('inject', help='inject message to picture')
    extract = subArgumentParser.add_parser('extract', help='extract message from picture')

    inject.add_argument('-f', type=str, required=True, metavar='--file', help='Image file path.')
    inject.add_argument('-m', type=str, required=True, metavar='--msg', help='Target message.')
    inject.add_argument('-o', type=str, required=True, metavar='--output', help='Output file path.',
                        default=DEFAULT_KEYS_PATH)
    inject.set_defaults(mode='inject')

    extract.add_argument('-f', type=str, required=True, metavar='--file', help='Image file path.')
    extract.add_argument('-k', type=str, required=True, metavar='--key-file', help='Keys file path.')
    extract.set_defaults(mode='extract')

    main(argumentParser.parse_args())
