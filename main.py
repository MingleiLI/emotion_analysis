## Author: Li Minglei
## Date: 13/11/2014
## Version: 1.0
## Description: The main function of emotion analysis

import affective_space
import conceptnet_matrix  
import word_embedding_nn
import numpy as np

#from scipy import linalg, mat, dot

# define affective space object
my_affective_space = affective_space.AffectiveSpace()
my_conceptnet = conceptnet_matrix.conceptnet()
my_word_embedding = word_embedding_nn.WordEmbeddingC()

# compute the consine similarity of two given vectors
def compute_cosine_sim(vector1, vector2):
    return np.inner(vector1, vector2)/np.linalg.norm(vector1)/np.linalg.norm(vector2)
 
# compute the consine similarity of two given concepts, the input should be string
def compute_concept_cos_sim(concept1, concept2):
    concept1_vector = my_affective_space.get_concept_vector(concept1)
    concept2_vector = my_affective_space.get_concept_vector(concept2)
    return compute_cosine_sim(concept1_vector, concept2_vector)

if __name__ == "__main__":
    queen_vector = my_affective_space.get_concept_vector("queen")
    king_vector = my_affective_space.get_concept_vector("king")
    man_vector = my_affective_space.get_concept_vector("man")
    woman_vector = my_affective_space.get_concept_vector("woman")
    diff_king_queen = king_vector - queen_vector
    diff_man_woman = man_vector - woman_vector
    
    print "In affectiveSpace:\n"
    print "The similarity of \"king - queen\" and \"man - woman\" is  " + str(my_affective_space.compute_cosine_sim(diff_king_queen, diff_man_woman))
    print "The similarity of \"party\" and \"gathering\" is " + str(my_affective_space.compute_concept_cos_sim("party","gathering"))
    print "The similarity of \"party\" and \"reception\" is " + str(my_affective_space.compute_concept_cos_sim("party","reception"))
    print "The similarity of \"party\" and \"man\" is " + str(my_affective_space.compute_concept_cos_sim("party","man"))
    print "The similarity of \"man\" and \"woman\" is " + str(my_affective_space.compute_concept_cos_sim("man","woman"))
    
    queen_vector2 = my_conceptnet.get_concept_vec("queen")
    king_vector2 = my_conceptnet.get_concept_vec("king")
    man_vector2 = my_conceptnet.get_concept_vec("man")
    woman_vector2 = my_conceptnet.get_concept_vec("woman")
    diff_king_queen2 = king_vector2 - queen_vector2
    diff_man_woman2 = man_vector2 - woman_vector2
    
    print "\nIn conceptnet:\n"
    print "The similarity of \"king - queen\" and \"man - woman\" is  " + str(compute_cosine_sim(diff_king_queen2, diff_man_woman2))
    print "The similarity of \"party\" and \"gathering\" is " + str(my_affective_space.compute_concept_cos_sim("party","gathering"))
    print "The similarity of \"party\" and \"reception\" is " + str(my_conceptnet.compute_concept_cos_sim("party","reception"))
    print "The similarity of \"party\" and \"man\" is " + str(my_conceptnet.compute_concept_cos_sim("party","man"))
    print "The similarity of \"man\" and \"woman\" is " + str(my_conceptnet.compute_concept_cos_sim("man","woman"))
    
    queen_vector3 = my_word_embedding.get_word_vec("queen")
    king_vector3 = my_word_embedding.get_word_vec("king")
    man_vector3 = my_word_embedding.get_word_vec("man")
    woman_vector3 = my_word_embedding.get_word_vec("woman")
    diff_king_queen3 = king_vector3 - queen_vector3
    diff_man_woman3 = man_vector3 - woman_vector3
    
    print "\nIn word Embedding:"
    print "The similarity of \"king - queen\" and \"man - woman\" is  " + str(compute_cosine_sim(diff_king_queen3, diff_man_woman3))
    print "The similarity of \"party\" and \"gathering\" is " + str(my_word_embedding.compute_word_cos_sim("party","gathering"))
    print "The similarity of \"party\" and \"reception\" is " + str(my_word_embedding.compute_word_cos_sim("party","reception"))
    print "The similarity of \"party\" and \"man\" is " + str(my_word_embedding.compute_word_cos_sim("party","man"))
    print "The similarity of \"man\" and \"woman\" is " + str(my_word_embedding.compute_word_cos_sim("man","woman"))


    


