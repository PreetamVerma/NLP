''' Sentiment Analysis @Naive Bayes Moddel
    
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
import sys
import math
import matrix_creator 
matrix_obj = matrix_creator.Matrix_Creator()


class Naive_Bayes_Classifier():

    def __init__(self):
        pass

    def Train_Naive_Bayes(self, prob_matrix, class_word_frequency, total_docs, V):
        pwc = {}
        for class_name, class_prior_prob in prob_matrix.items(): 
            for each_word in V[:]:
                w_c = class_word_frequency[class_name].get(each_word, 0)
                class_words = len(class_word_frequency[class_name].keys())   
                pwc[each_word, class_name] =  math.log10(float(w_c + 1)/(len(V) + class_words))
        return pwc  
            
    def Test_Naive_Bayes(self, test_doc, log_prior, loglikelihood, C, V):
        ''' return best c for c belongs C'''
        sum_c = {}
        for each_class in C:
            sum_c[each_class] = log_prior[each_class]
            for i, each_word in enumerate(test_doc.split(" ")): 
                if each_word in V: 
                    sum_c[each_class] = sum_c[each_class] + loglikelihood[each_word, each_class]
                else:print('word %s not found'%(each_word))
        best_class = ''
        num = None
        for k , v in sum_c.items():
            if not num:
                num = v
                best_class = k
            if num < v:
                best_class = k 
        return best_class

    def process_basic(self, fname):
        total_docs, class_word_frequency, log_prior, V = matrix_obj.process_basic(fname)
        loglikelihood  = self.Train_Naive_Bayes(log_prior, class_word_frequency, total_docs, V)
        #test_doc = 'Loved the casting of Jimmy Buffet as the science teacher, but i hate him as a person.'
        test_doc = 'Saw the movie today and thought it was a good effort, bad messages for kids'
        #test_doc  = 'Rahul Gandhi may visit as many temples, but the BJP will remain the original pro-Hindutva party, this was the message conveyed to the Congress on '

        C = ['positive', 'negative']  
        best_class = self.Test_Naive_Bayes(test_doc, log_prior, loglikelihood, C, V)
        print ('=============\n')
        print ('==========input_str', test_doc) 
        print ('========== best_class ', best_class) 
      

if __name__ == '__main__':
    obj = Naive_Bayes_Classifier()
    fname = "../../../input/imdb_labelled.txt"
    obj.process_basic(fname) 
