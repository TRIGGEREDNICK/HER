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
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class Encoder:

    """
    HER Encoder
    """

    def __init__(self, HERDict):
        # It declares the list
        # of the HER document
        # lines.
        self.HERString = []
        # It calls the parseDictionary,
        # that will store the list
        # into self.HERString.
        self.parseDictionary(HERDict)
        # It creates the string,
        # joining the content using
        # the \n character.
        self.HER = "\n".join(self.HERString)

    def parseDictionary(self, HERDict):
        # The "for-each" starts
        for key, value in HERDict.items():
            # It appends the
            # Category to the
            # HER Document lines List.
            self.HERString.append("- " + key + " -")
            # Another "for-each" starts,
            # it will read the values of the category,
            # the sub-values of the entire
            # Dictionary.
            for subkey, subvalue in value.items():
                # It checks if the sub-value
                # is a list.
                if isinstance(subvalue, list):
                    # It's a list, so
                    # it declares the list
                    # using HER Syntax.
                    self.HERString.append("    >> " + str(subkey) + "[]")
                    # Another "for-each" starts,
                    # it will read the values of the
                    # ipotetic list (sub-value of the sub-value),
                    # we will call them: "tunnelvalues"
                    for tunnelvalue in subvalue:
                        # It checks if the
                        # tunnelvalue is a string.
                        if isinstance(tunnelvalue, str):
                            # It's a string, so
                            # it escapes it and
                            # it assigns the value
                            # to listvalue.
                            listvalue = "\"" + str(
                                tunnelvalue).replace('"',
                                                     '\"').replace("'",
                                                                   "\'") + "\""
                        # Then, if it isn't
                        # a string, it doesn't
                        # escape anything.
                        else:
                            # It just assigns
                            # the value to
                            # listvalue.
                            listvalue = tunnelvalue
                        # It appends the listvalue,
                        # just the escaped tunnelvalue,
                        # to HER Document lines List.
                        self.HERString.append(
                            "    * " + str(
                                subkey) + "[] = " + str(
                                    listvalue))
                # Then, if it isn't
                # a list, it just
                # uses the HER Syntax and
                # append the key-value (variable).
                else:
                    # It checks if it's
                    # a string
                    if isinstance(subvalue, str):
                        # It's a string, so
                        # it escapes it and
                        # it assigns the value
                        # to listvalue.
                        listvalue = "\"" + str(
                            subvalue).replace('"',
                                              '\"').replace("'",
                                                            "\'") + "\""
                    # Then, if it isn't
                    # a string, it doesn't
                    # escape anything.
                    else:
                        # It just assigns
                        # the value to
                        # listvalue.
                        listvalue = subvalue
                    # It appends the listvalue,
                    # just the escaped subvalue,
                    # to HER Document lines List.
                    self.HERString.append(
                        "    * " + str(
                            subkey) + " = " + str(
                                listvalue))
