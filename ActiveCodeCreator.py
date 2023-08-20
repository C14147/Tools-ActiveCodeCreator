"""
Active Code Creator.py
------------------------------------------------------------------------
Version: 1.0.02a

Copyright 2020-2023 WorkFlow Corporation
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:
        http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
express or implied.
See the License for the specific language governing permissions and
limitations under the License.

1. The code is optimized according to the PEP8 specification
2. Fix an error when the program accepts parameters
3. An API interface has been added to allow other programs to generate strings using the ‘generate(int length)’ function.
4. Optimize the generated dictionary
5. Optimizations reduce program space complexity

Introduction:
  Pass in the '--length [number]' parameter to generate a random
  of corresponding length.
"""


import argparse
from sys import *
from random import choice


# set & get args
parser = argparse.ArgumentParser()
parser.add_argument(
    "length", 
    default=10,
    type = int,
    help="generate a random of corresponding length."
)
args = parser.parse_args()
a = [    # keys
    "A", "a", "B", "b",
    "C", "c", "D", "d",
    "E", "e", "F", "f",
    "1", "2", "3", "4",
    "5", "6", "7", "8",
    "9", "!" , "=", "?",
    "{" , "}", "<",  ">",
    "[" , "]", "(",  ")",
]


# The generate function
def generate(length: int) -> str:
    _data = []
    for i in range(int(length)):
        _data.append(choice(a))
    return _data

if __name__ == "__main__":
    print(generate(args.length))
