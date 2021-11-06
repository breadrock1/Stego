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

from pathlib import Path
from argparse import ArgumentParser

from src.MessageExtractor import MessageExtractor
from src.MessageInjector import MessageInjector


PROJECT_ROOT_DIR = Path()


def main():
    argumentParser = ArgumentParser(
        prog='StegProject',
        usage='''./launch.py MODE {inject | extract} -f <picture-file-path>
                Mode details (Select one of those methods and '--help' to get more information about options):
                1. inject   - This mode provides ability to inject specified by user message to specified picture;
                        -m <message-string> [-o <output-key-file-path>]
                2. extract  - This mode provides ability to extract message from specified picture by specified key-file.
                        -k <key-file-path>
            ''',
        description='''
                This simple python script provides ability to inject/extract message to/from picture.
            ''',
        add_help=True,
        allow_abbrev=True
    )

    mode = None

    subArgumentParser = argumentParser.add_subparsers(title='Script Mods', dest=mode)
    inject = subArgumentParser.add_parser('inject', help='inject message to picture')
    extract = subArgumentParser.add_parser('extract', help='extract message from picture')

    inject.add_argument('-f', type=str, required=True, metavar='--picture', help='Image path to store msg')
    inject.add_argument('-m', type=str, required=True, metavar='--msg-string', help='Message to store')
    inject.add_argument('-o', type=str, required=True, metavar='--output-file', help='Output file with key',
                        default=PROJECT_ROOT_DIR / 'resources' / 'keys.txt')

    extract.add_argument('-f', type=str, required=True, metavar='--picture', help='Image path to store msg')
    extract.add_argument('-k', type=str, required=True, metavar='--key-file', help='File with key to extract msg')

    inject.set_defaults(mode='inject')
    extract.set_defaults(mode='extract')

    arguments = argumentParser.parse_args()

    if mode is "inject":
        messageInjector = MessageInjector()
        messageInjector.inject_message(
            image_path=arguments.f,
            keys_file_path=arguments.o,
            user_message=arguments.m
        )

    elif mode is "extract":
        messageExtractor = MessageExtractor()
        messageExtractor.extract_message(
            image_path=arguments.f,
            keys_file_path=arguments.k
        )

    else:
        argumentParser.print_usage()


if __name__ == "__main__":
    main()
