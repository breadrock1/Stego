# Stego Project

![GitHub](https://badgen.net/badge/icon/github?icon=github&label)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![GitHub version](https://img.shields.io/badge/version-v1.2.0-green?style=plastic&labelColor=dark)
[![Building Project](https://github.com/breadrock1/Stego/actions/workflows/build-project-action.yml/badge.svg?branch=master)](https://github.com/breadrock1/Stego/actions/workflows/build-project-action.yml)

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
Usage: python3 stego.py { inject [options] | extract [options] } -f <picture-file-path>
            
            There are two modes to use this simple application:
            
            1. inject  - Allows to inject passed string message to stego-container. There are 
                         following additional needed options: 
                                -m <message-string> [-o <output-key-file-path>]

            2. extract - Allows to extract string message from stego-container. Just pass key 
                         file path: -k <key-file-path>

            For mode details for each other modes enter '--help'.

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
