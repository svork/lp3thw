from sys import argv
from os.path import exists

script, from_file, to_file = argv

entrada = open(from_file).read()

saida = open(to_file, 'w').write(entrada)
