import nltk
from nltk.corpus import treebank

class HMM_Tagger(object):

    def __init__(self):
        pass

    def get_emmision_probability(self, pos_tag_dict, emmision_dict):
        emmision_state_arr = []
        for key, val in emmision_dict.items():
           prob = float(val/pos_tag_dict[key[1]]*1.0) 
           emmision_state_arr.append([key, val, prob])
        emmision_state_arr = sorted(emmision_state_arr, key=lambda x:x[-1])                                   
        return emmision_state_arr

    def get_transition_probabilty(self, pos_tag_dict, transaction_dict):
        all_pos_tags = list(pos_tag_dict.keys())
        transaction_state_arr = [] 
        dup_dict = {}
        for i, each_pos_tag_1 in enumerate(all_pos_tags):
            for j, each_pos_tag_2 in enumerate(all_pos_tags):
               if (i<j):
                   key = (each_pos_tag_1, each_pos_tag_2)
                   if dup_dict.get(key, 0):
                      continue
                   pos_tag_cnt = pos_tag_dict[each_pos_tag_1]
                   key_cnt = transaction_dict.get(key, 0)
                   transaction_state_arr.append([each_pos_tag_1, key, ("key_cnt", key_cnt, "pos_tag_cnt", pos_tag_cnt), float(key_cnt*1.0 / pos_tag_cnt*1.0)])

        transaction_state_arr = sorted(transaction_state_arr, key=lambda x:x[-1])                                   
        return transaction_state_arr   

    def get_word_tag_probabilty(self, word, pos_tag_dict, transaction_dict):
        all_pos_tags = list(pos_tag_dict.keys())
        for pos_tag in all_pos_tags:
           key = (word, pos_tag)
           pass

    
    def process_basic(self):
        word_list = list(treebank.tagged_words()) 
        transaction_dict = {}
        emmision_dict = {} 
        pos_tag_dict  = {}
        for i in range(1, len(word_list), 2):
            word_tuples = (word_list[i-1], word_list[i])
            tag1, tag2 = word_list[i-1][1], word_list[i][1]

            if not pos_tag_dict.get(word_list[i-1][1], 0):
               pos_tag_dict[word_list[i-1][1]] = 0   
            if not pos_tag_dict.get(word_list[i][1], 0):
               pos_tag_dict[word_list[i][1]] = 0   
            pos_tag_dict[word_list[i-1][1]] +=1
            pos_tag_dict[word_list[i][1]] +=1
            
            if not  transaction_dict.get((word_tuples[0][1], word_tuples[1][1]), 0):
                transaction_dict[(word_tuples[0][1], word_tuples[1][1])] = 0 
            transaction_dict[(word_tuples[0][1], word_tuples[1][1])] += 1 
                 
            if not emmision_dict.get(word_tuples[0], 0):
                emmision_dict[word_tuples[0]] = 0 
            emmision_dict[word_tuples[0]] += 1 
            
            if not emmision_dict.get(word_tuples[1], 0):
                emmision_dict[word_tuples[1]] = 0 
            emmision_dict[word_tuples[1]] += 1 
           
        transaction_state_arr = self.get_transition_probabilty(pos_tag_dict, transaction_dict) 
        emmision_state_arr = self.get_emmision_probability(pos_tag_dict, emmision_dict) 
        for each in emmision_state_arr[::-1]:
           print ("\t\t each", each)
                                  
if 1:
   HMM_Tagger().process_basic()
