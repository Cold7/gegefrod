#importing libraries

import sys 
import argparse
import time
import pandas as pd

#defining functions
def done():
	print ("Done (Date: "+str(time.strftime("%y/%m/%d"))+" Time: "+str(time.strftime("%H:%M:%S"))+")")
	exit()


	
if __name__ == "__main__":


	print("\n\n#####################################")
	print("##                                 ##")
	print("##              gEGeFroD           ##")
	print("## get Expression Gene From Deseq2 ##")
	print("##            version 3.0          ##")
	print("##                                 ##")
	print("##             Created by          ##")
	print("##   Sebastian Contreras-Riquelme  ##")
	print("##   Search me on github as Cold7  ##")
	print("##                                 ##")
	print("#####################################\n\n")
	
	#checking python version
	if (sys.version_info < (3, 0)):
		print("You are using a python version lower than 3.0. Please use python3 to execute this script. Exiting")
		exit()

	#input
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--deseq2_output_file", help="Deseq2 result file.", required=True)
	parser.add_argument("-c","--condition_name", help="Condition column name to select columns", required=True)
	parser.add_argument("-g","--gene_name", help="Gene column name to select columns. Default: gene", default="gene")
	parser.add_argument("-f","--output_file", help="Output file to save results. Default = ./output", default="./output")
	parser.add_argument("-m","--minCount", help="minimum number of counts to consider. Default = 10", default=10, type=int)
	
	
	args = parser.parse_args()


	print("Starting gEGeFroD.py (Date: "+str(time.strftime("%y/%m/%d"))+" Time: "+str(time.strftime("%H:%M:%S"))+") using the following parameters:")
	print("  DEseq2 result file: "+args.deseq2_output_file)
	print("  Condition column name: "+args.condition_name)
	print("  Gene column name: "+args.gene_name)
	print("  Output File: "+args.output_file)
	print("  Minimum number of counts: "+str(args.minCount))
	print("\n")

	columnsToUse = []
	df = pd.read_csv(args.deseq2_output_file)
	outFile = open(args.output_file,"w")
	#getting conditions names
	for column in df.columns:
		if args.condition_name in column:
			columnsToUse.append(column)
	for i in range(len(df[columnsToUse[0]])):
		minCountAproved = True
		average = 0
		for column in columnsToUse:
			if float(df[column][i]) < args.minCount:
				minCountAproved = False
			average += float(df[column][i]) #to compute an average
		if minCountAproved == True:
			average = average/len(columnsToUse)
			outFile.write(df[args.gene_name][i]+"\t"+str(average)+"\n")
	outFile.close()
	done()
	


