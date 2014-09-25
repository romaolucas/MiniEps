import re
import sys
import os


class Erro(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Conversor():
    exp1 = re.compile("\s*\$\w+\s+(\d+|\w+)")
    exp2 = re.compile("\s*(\@|\w+)\s+[\w.\s]+\(")
    exp3 = re.compile("\s*(\d+|\d+[MHDW])\s*[;)]")
    exp4 = re.compile("\s*(IN)?\s*NS\s+\w")
    exp5 = re.compile("\s*\w+\s+IN\s+A\s+(\d+[.]?)+")
    fqdn = ""

    def __init__(self, arquivoEntrada, arquivoSaida="saida"):
        sys.stdin = open(arquivoEntrada, "r")
        sys.stdout = open(arquivoSaida, "w")

    def converte(self):
        for line in sys.stdin:
            if self.exp1.match(line) != None or self.exp2.match(line) != None \
                    or self.exp3.match(line) != None:
                print(line, end="")
            elif self.exp4.match(line) != None:
                print(line)
                v = line.split()
                fqdn = v[len(v) - 1].split(".", 1)

