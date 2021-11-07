# Stego Project

![GitHub](https://badgen.net/badge/icon/github?icon=github&label)
![version](https://img.shields.io/badge/version-1.1-blue)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)

## What Is Steganography?
Steganography is the practice of hiding a secret message inside of (or even on top of) something that is not secret. That something can be just about anything you want. These days, many examples of steganography involve embedding a secret piece of text inside of a picture. Or hiding a secret message or script inside of a Word or Excel document.

The purpose of steganography is to conceal and deceive. It is a form of covert communication and can involve the use of any medium to hide messages. It’s not a form of cryptography, because it doesn’t involve scrambling data or using a key. Instead, it is a form of data hiding and can be executed in clever ways. Where cryptography is a science that largely enables privacy, steganography is a practice that enables secrecy – and deceit.

## Setting up

To setting up environment to run this script use this bash command:

```bash
    pip install -r requirements.txt
```

## Usage

```bash
Usage: ./launch.py MODE {inject | extract} -f <picture-file-path> -h help

  Mode details (Select one of those methods and '--help' to get more information about options):
    1. inject   - This mode provides ability to inject specified by user message to specified picture; 
                    -m <message-string> [-o <output-key-file-path>]
    2. extract  - This mode provides ability to extract message from specified picture by specified key-file.
                    -k <key-file-path>

There's a small script that provides an ability to hide message text to the specified BMP format picture and extract it back by key.
```

## License 

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

## TODO

1. Adding ability to specify file path with a message;
2. Realise pytest UnitTest.
