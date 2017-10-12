from bz2 import BZ2File 
 
path ='E:\database work\wikidata,josn.bz2'
path2='E:\database work\test.josn'

r_file=BZ2File(path,'r')
w_file=open(path2,'w')
for i in range(3):
    w_file.write(r_file.readline())

r_file.close()
w_file.close()