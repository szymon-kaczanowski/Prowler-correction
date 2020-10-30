import pandas as pd
import numpy as np
import re as re
# Standard library package
import io
import os

# Import Biopython modules to interact with KEGG
from Bio import SeqIO
from Bio.KEGG import REST
from Bio.KEGG.KGML import KGML_parser
import sys

def  kooo(cccc):
     mydog5=""
     mydog = REST.kegg_find("genes", cccc).read()
     #print(result)
     mydog1 = re.findall('^\S+',mydog)[0]
     #print(mydog1)
     mydog3 = REST.kegg_link("ko", mydog1).read()
     print("xxx",mydog3)
     if(len(mydog3)<4):
         return(mydog5)    
     mydog4=re.findall('ko:\S+',mydog3)[0]
     #print(mydog4)
     mydog5 = REST.kegg_link("genes", mydog4).read()   
     return(mydog5)

def unique(list1):
    x = np.array(list1)
    return(np.unique(x))

def specie_kegg(dddd):
    mydog6=re.findall('[a-z]+',dddd)
    return(mydog6)

a=REST.kegg_info('genes').read()
#print(a)
#print(kooo("YBR248C"))


#print(unique(specie_kegg(kooo("YBR248C"))))

def specie_kegg1(ddd):
    return(specie_kegg(kooo(ddd)))


specie=pd.read_pickle('specie')

def two_words(input):
    return(re.findall('^\S+[ ]*\S*',str(input))[0])

def longer_name(input):
    p=re.compile('[ ]*\([\S ]+')
    input1=p.sub('',str(input))
    return(input1)


specie['Organisms.2']=specie['Organisms.1'].apply(two_words)
specie['Organisms.3']=specie['Organisms.1'].apply(longer_name)
#specie.applymap(lambda x: re.findall('^\S+[ ]*\S*',str(x))[0])
specie['Organisms']



#print(sys.argv[1])
with open(sys.argv[1]) as f:
    species = f.read().splitlines()

with open(sys.argv[2]) as f:
    list_of_genes = f.read().splitlines()



def specie_name(name):
    c=0
    c=specie['Organisms'][(specie['Organisms.2']==name)].values[0]
    return(c)
sp1=[]  
for sp in species:
    #print(sp,specie_name(sp))
    sp1.append(specie_name(sp))
sp1

def compare_lists(input1, input2):
  #return(input1) 
  output=[]
  len(output)  
  for i in range(len(input1)):
          if (input1[i] in input2): 
            output.append('+')
          else:
            output.append('-')
  return(output)     

def append1(input_frame,input_columns,input_values):
          frame_output=pd.DataFrame([input_values],columns=input_values)
          frame_output1=input_frame.append(frame_output)
          return(frame_output1)

species_extend=['gene name']+species
#print(species_extend)
#sp1=[]
def profile_gene(gene_name):
    #species_extend=['gene name']+species
    pp1=[]
    pp1 += [gene_name]
    profile_extend=pp1+compare_lists(sp1,specie_kegg1(gene_name))
    print(profile_extend)
    frame1=pd.DataFrame([profile_extend],columns=species_extend)
    return(frame1)

def profile_gene_list(list_of_genes):
    species_extend=['gene name']+species
    frame0=pd.DataFrame(columns=species_extend)
    for gene in list_of_genes: 
         frame0=frame0.append(profile_gene(str(gene)))
    return(frame0)


wynikowy=profile_gene_list(list_of_genes)

wynikowy.xls=sys.argv[3]+'.xlsx'
#print(wynikowy.xls)

wynikowy.to_excel(wynikowy.xls,
             sheet_name='Sheet_name_1')
wynikowy.tsv=sys.argv[3]+'.tsv'
wynikowy.to_csv(wynikowy.tsv, sep='\t')

#print(pd.DataFrame([species_extend],columns=species_extend))
#print(profile_gene("YBR248C"))


#print(species)


