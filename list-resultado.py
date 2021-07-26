# -*- coding: utf-8 -*-
 '''\
    Read a list of lines from a file line by line into an output file.
    only 10 first lines
'''

with open("resultado_part-00000.txt", 'r', encoding="utf8") as infile:
    data = infile.read().split('\n')
    data = data[:10]
    output = ""
    output = '\n'.join(data)

with open('resultado.txt', 'w') as outfile:
    outfile.write(output)
