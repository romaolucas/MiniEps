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

    def __init__(self, arquivoEntrada, arquivoSaida="saida"):
        try:
            sys.stdin = open(arquivoEntrada, "r")
            sys.stdout = open(arquivoSaida, "w")
        except FileNotFoundError:
            sys.exit("Erro na leitura do arquivo!")


    def converte(self):
        fqdn = ""
        for line in sys.stdin:
            if self.exp1.match(line) != None or self.exp2.match(line) != None \
                    or self.exp3.match(line) != None:
                print(line, end="")
            elif self.exp4.match(line) != None:
                print(line)
                v = line.split()
                fqdn = v[len(v) - 1].split(".", 1)
            elif self.exp5.match(line) != None:
                v = line.split()
                aux = v[len(v) - 1].split(".")
                txt = "" + aux[len(aux) - 1] + "    IN PTR"
                txt += "    " + v[0] + "." + fqdn[1] + "\n"
                print(txt)

