import sys 

#table with the tAI value for each codon 
tAI_Table = { 
'AAC': 1, 
'UGC': 0.886100386, 
'GCU': 0.844594595, 
'AAG': 0.733590734, 
'AAU': 0.617760618, 
'CAG': 0.616795367, 
'GCC': 0.608108108, 
'AUU': 0.543918919, 
'UGU': 0.536679537, 
'GUG': 0.488416988, 
'AAA': 0.482625483, 
'AUC': 0.474903475, 
'GAA': 0.41023166, 
'UAC': 0.403474903, 
'UUC': 0.386100386, 
'GAC': 0.386100386, 
'GAG': 0.372586873, 
'GGC': 0.361969112, 
'GGG': 0.359073359, 
'AUG': 0.28957529, 
'CUG': 0.272200772, 
'CUU': 0.265444015, 
'CCU': 0.255550193, 
'UAU': 0.251930502, 
'GCA': 0.241397201, 
'GUU': 0.241312741, 
'UCU': 0.241312741, 
'ACU': 0.241312741, 
'CAC': 0.241312741, 
'UUU': 0.227799228, 
'GAU': 0.227799228, 
'GGA': 0.217181467, 
'UUG': 0.215250965, 
'GGU': 0.213561776, 
'AGC': 0.21042471, 
'CCC': 0.197876448, 
'GCG': 0.197876448, 
'CAA': 0.193050193, 
'UGG': 0.193050193, 
'CUC': 0.191119691, 
'ACG': 0.191119691, 
'GUC': 0.173745174, 
'UCC': 0.173745174, 
'ACC': 0.173745174, 
'GUA': 0.16894305, 
'CCA': 0.16894305, 
'CGU': 0.168918919, 
'AGG': 0.166988417, 
'CCG': 0.150579151, 
'ACA': 0.144811776, 
'CGA': 0.144804537, 
'UUA': 0.144787645, 
'AGA': 0.144787645, 
'CGG': 0.142857143, 
'CAU': 0.142374517, 
'AGU': 0.138030888, 
'UCG': 0.127413127, 
'CGC': 0.121621622, 
'AUA': 0.12070222, 
'CUA': 0.096551641, 
'UCA': 0.096549228 
} 

notFound = {} #codons not found in the table 

def evaluate(codons, table): 
	netCharge = 0.0 
	number = 0 
    #for each sequence of 3 characters 
	size = int(len(codons)/3) 
	for i in range(size): 
		seq = '' 
		k = i*3 
    	#read the next 3 caracteres 
		for j in range(3): 
			seq += codons[k+j] 
         #compute the sequence value from the tAI table 
			if seq.upper() in table:
        	#table.has_key(seq.upper()): 
				charge = table[seq.upper()] 
				netCharge += charge 
				number +=1 
			else: #case the sequence was not found in the tAI table 
				if not seq.upper() in notFound:
					notFound[seq.upper()] = 1 
				else: 
					notFound[seq.upper()] += 1      
	if number > 0:      
		output = str(netCharge) + ',' + str(number) + ',' + str(netCharge/number) + '\n'     
	if number <= 0:
		output = str(netCharge) + ',' + str(number) + ',' + str(netCharge/1) + '\n'     
	return output 

#main function 
def main(): 
	names = [] 
	#read the program arguments 
	if len(sys.argv) < 3: 
		print("Use: python", sys.argv[0], "<input file name>", "<output file name>")               
		sys.exit(0) 

	filein = sys.argv[1] #input file name 
	fileout = sys.argv[2] #output file name 

	#read the file's contents 
	fin = open(filein, 'r') 
	contents = fin.read() 

	#open the output file 
	fout = open(fileout, 'w') 
	fout.write("Gene name" + ',' + "Gene ID" + "," + "tAI" + ',' + "number of codons found in table" + ',' + "tAI/number of codons" +'\n') #,' 
     
    #split the file's contents by '\n' 
	codons = str.split(contents, '\n')[1:-1] #the file header and last empty item are discarded 
	for cod in codons: 
		lista = str.split(cod, '\t') #split each sequence by \t
		fout.write(lista[0] + ',' + lista[1] + ',' + evaluate(lista[5], tAI_Table))

	fin.close()

	fout.close() 
	print('Sequences not found in the tAI Table:') 
	print(notFound) 
	print('Done!')

main() 
