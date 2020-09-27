#!/usr/bin/python3


with open("/home/giacomo/Documenti/ML/KaggleV2-May-2016.csv",'r') as f:
    with open("/home/giacomo/Documenti/ML/KaggleV2-May-2016_tagliato.csv",'w') as f1:
    	count = 0
    	count_scritte = 0
    	for line in f:
        	#print("dentro il ciclo\n")
        	linea_splittata = line.split(',')
        	#print(len(linea_splittata[13].replace("\n","")))
        	#print(linea_splittata[13])
        	if (linea_splittata[13]=="No\n" and count<44000):
        		print(f'NoShow:{linea_splittata[13]} linea taglia numero {count}\n')
        		#next(f)
        		count += 1
        	else:
        		#print("scrittura rifga\n")
        		count_scritte +=1
        		f1.write(line)
        		print(f'scritte: {count_scritte}')
print(f'Linee cancellate: {count}	line scritte: {count_scritte}')