# This file is a part of HER
#
# Copyright (c) 2017 The HER Authors (see AUTHORS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class Decoder:

    """
    HER Decoder
    """
    def __init__(self, HERString, isFile = False):
        if isFile is True:
            HERString = HERString.readlines()
        else:
            HERString = HERString.splitlines()
        content = [x.strip() for x in HERString]
        currentSection = ""
        HER = {}
        for line in content:
            if line.startswith("#"):
                continue
            elif line.startswith("- "):
                currentSection = line[2:-2]
                HER[currentSection] = {}
            elif line.startswith(">> "):
                if line.split(" =")[0][-2:] == "[]":
                    HER[currentSection][line.split("[] =")[0][3:-2]] = []
            elif line.startswith("* "):
                if line.split(" =")[0][-2:] == "[]":
                    exec("HER[currentSection][line.split(\" =\")[0][2:-2]].append(" + line.split(" = ")[1] + ")")
                else:
                    exec("HER[currentSection][line.split(\" =\")[0][2:]] = " + line.split(" = ")[1])
        self.HER = HER
