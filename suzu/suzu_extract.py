import os

def read_bin(filename, offset, length):
    with open(filename, 'rb') as file:
        file.seek(offset)
        data = file.read(length)
    return data

def read_bin2(filename, offset):
    with open(filename, 'rb') as file:
        file.seek(offset)
        data = file.read()
    return data

def write_bin2(filename, offset, data):
    with open(filename, 'r+b') as file:
        file.seek(offset)
        file.write(data)

def write_bin(filename, offset, data):
    with open(filename, 'wb') as file:
        file.seek(offset)
        file.write(data)

def extract(resfile, binfile, outdir):
    hex_values = []
    with open(resfile, "r") as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 3:
                hex_value = columns[1]
                hex_values.append(int(hex_value, 16))

    i = 0
    while i < len(hex_values)-2:
        start = hex_values[i]
        l = hex_values[i+1]-start
        dat = read_bin(binfile, start, l)
        write_bin(f'{outdir}/{i}.bmp', 0x0, dat)
        i+=1
    start = hex_values[i]
    write_bin(f'{outdir}/{i}.bmp', 0x0, read_bin2(binfile, start))

def combine(directory, outfile, resfile):
    hex_values = []
    with open(resfile, "r") as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 3:
                hex_value = columns[1]
                hex_values.append(int(hex_value, 16))
    nf = 0
    for i in range(0, len(hex_values)-2):
        file_path = os.path.join(directory, f'{i}.bmp')
        with open(file_path, 'rb') as bf:
            fd = bf.read()
            write_bin2(outfile, hex_values[i], fd)
            nf += len(fd)-hex_values[i]

#extract('res/dat.txt', 'res/SUZU', 'suzu_out')
#combine('suzu_out', 'SUZU', 'res/dat.txt')