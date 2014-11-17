#Author Li Minglei
#Emali: liminglei29@gmail.com
#Des: Process the AffectiveSpace file
#Date: 12/11/2014
#Version: 1.0
# howto summit to github??

import numpy as np


###################################################################
## class AffectiveSpace ###
## data source:
## http://sentic.net/downloads/
###################################################################

class AffectiveSpace(object):
    """
    
    The AffectiveSpace related function, including concept finding, concept similarity, etc.
    
    """

#open the source with csv module
#read the affectiveSpace file
    def __init__(self):
        import csv
        affective_file = open("/mnt/hgfs/Corpus_resource/senticNet/affectivespace/affspace_23243_100.csv", "rb")
        affective_space_data = csv.reader(affective_file)

#get the concept number
        concept_num = affective_space_data.line_num
        concept_vector_dim = 100

#convert the csv data into dictionary with the concepts as key and the related value as key value
        self.__concept_lis = []
        for row in affective_space_data:
        	self.__concept_lis.append(row[0])
#concept_vector.append(map(float, row[1:]))#convert string to float
#convert the string list to float list
#concept_vector = list(map(float, concept_vector)) #convert string to float
        affective_file.close()

#open the source with numpy module, the last row in the source file has some problem, so we just skip the last row.
        vec_cols = [x for x in range(1,concept_vector_dim+1)] #the first column are concepts
        self.__concept_matrix = np.genfromtxt("/mnt/hgfs/Corpus_resource/senticNet/affectivespace/affspace_23243_100.csv",dtype=float, skip_footer=1, delimiter=',', usecols=vec_cols)




#Check whether a concept is contained in the AffectiveSpace
    def check_concept(self, concept):
        if concept in self.__concept_lis:
            return True
        else: 
            return False


#define the function to read a vector of a given concept
    def get_concept_vector(self, concept):
        try:
            index = self.__concept_lis.index(concept)
            return self.__concept_matrix[index]
        except ValueError:
            print "concept \"" + concept + "\" is not contained in AffectiveSpace, try again\n"
            return False


























