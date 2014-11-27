#Author Li Minglei
#Emali: liminglei29@gmail.com
#Des: Process the ConceptNet matrix
#Date: 12/11/2014
#Version: 1.0
#source: https://github.com/commonsense/divisi2/blob/master/doc/tutorial_aspace.rst


import divisi2


class conceptnet(object):
    '''
    The conceptnet matrix related operation, such as concept similarity computing, geting the concept vector, etc...

    '''
    def __init__(self):
#get the original sparce matrix
        self.__conceptnet = divisi2.load('/opt/work/emotion_analysis/data_source/conceptnet_en.pickle')

#Get the matrix after svd
        self.__concept_axes, self.__axis_weights, self.__feature_axes = self.__conceptnet.svd(k=100)

#Get the similarity operator
        self.__sim = divisi2.reconstruct_similarity(self.__concept_axes, self.__axis_weights, post_normalize=True)

#conpute the similarity of two concepts
    def compute_concept_cos_sim(self, concept1, concept2):
        try:
            return self.__sim.entry_named(concept1,concept2)

        except KeyError:
            print "There is no concept \"" + concept1 + " \" or \" " + concept2 + "\"!\n"
#get the vector of the given concept
    def get_concept_vec(self, concept):
        try:
            return self.__concept_axes.row_named(concept)
        except KeyError:
            print "There is no concept \"" + concept + "\"!\n"






