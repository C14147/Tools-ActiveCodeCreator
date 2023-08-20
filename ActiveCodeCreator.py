#! python3
#   Copyright 2020-2023 WorkFlow Corporation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at:
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Active Code Creator.py
--------------------------------------------------------
Version: 1.0.02a
By Li Zhengyi(China)
Introduction:
  Pass in the '-- len' parameter to generate a random
  string of corresponding length.
"""
from sys import *
from random import randint
a = [
    "a","b",
    "c","z",
    "Y","y",
    "S","s",
    "O","o",
    "F","f",
    "T","t",
    "W","w",
    "A","a",
    "R","r",
    "E","e",
    "?","=",
    "*","@",
]
ra = 10
if len(argv) > 1:
    ra = int(argv[1])
for i in range(ra):
    print(a[randint(0,25)],end="")
