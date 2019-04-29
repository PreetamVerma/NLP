''' Sentiment Analysis @Naive Bayes Moddel
    
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
import sys
import re
import math

class Matrix_Creator():

    def __init__(self):
        self.stop_words = list(set(stopwords.words('english')))
        pass

    def read_data_set(self, fname = None):
        if not fname:return []
        lines = map(lambda x:x.strip(), open(fname).readlines()[:])
        return lines 
        

    def create_data_dict(self, data_list):
        tmp_dict = {} 
        
        for each in data_list:
           sentence, category = each.split("\t")   
           if not tmp_dict.get(category, []):
               tmp_dict[category] = []
           tmp_dict[category].append(sentence) 
        return tmp_dict   

    def get_class_word_matrix(self, data_list):
        clas_word_frequency = {} 
        for each in data_list:
            sentence, category = each.split("\t")   
            if not clas_word_frequency.get(category, {}):
                clas_word_frequency[category] = {}
            words = []
            for word in sentence.split():  
               word = word.lower()
               word = word.replace('"', "") 
               word = word.replace('.', "") 
               word = word.replace("'", "") 
               word = word.replace("/", "")
               word = word.replace(",", "")
               if (word.strip() and word.strip() not in self.stop_words) and len(word) >2: 
                   words.append(word)
            
            for each_word in words:
               if not clas_word_frequency[category].get(each_word, 0):
                   clas_word_frequency[category][each_word] = 0
               clas_word_frequency[category][each_word] += 1
               
        V = []
        for k,  v in clas_word_frequency.items():
            V = V + clas_word_frequency[k].keys()[:]    
              
        return clas_word_frequency, V  
   
  
    def process_basic(self, fname):
        data_list   =  self.read_data_set(fname)
        total_docs  = len(data_list) 
        clas_word_frequency, V = self.get_class_word_matrix(data_list)
        p_class_dict  = self.create_data_dict(data_list)
        prob_matrix = {}
        for category, sentence_list in p_class_dict.items():
           prob_matrix[category] =  math.log10(float(len(sentence_list)) /total_docs) 
            
        return total_docs, clas_word_frequency, prob_matrix , V   
         

if __name__ == '__main__':       


    obj = Matrix_Creator()
    obj.process_basic("../input_data/sentiment_labelled_sentences/imdb_labelled.txt") 
