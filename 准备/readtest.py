from bz2 import BZ2File, BZ2Decompressor

path = "E:\database work\wikidata.json.bz2"
path2 = '''E:/database work/test.json'''

read_file = BZ2File(path, 'r')
with open(path2, 'wb') as write_file:
    for i in range(10):
        write_file.write(read_file.readline())

