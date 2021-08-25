import string
import re
import numpy as np
import math

class Inverted_Index:
    def __init__(self, FILENAME):
        self.FILENAME = FILENAME
        # dictionary from docID to docTitle
        self.docs = {}

        # magnitude of tf vector of each document 
        self.magnitude = dict()
        
        # term -> posting list dictionary  
        self.InvertedIndex = {}

        self.initialize()
    


    class PostingList:
        def __init__(self, docID):
            self.head = self.Node(docID)
            self.tail = self.Node(docID)

        # adding a word to the posting list 
        def add(self, docID):
            if self.tail.docID == docID:
                if self.head.docID == self.tail.docID:
                    self.head.tf += 1
                self.tail.tf += 1
            else:
                temp = self.Node(docID)
                if self.head.docID == self.tail.docID:
                    self.head.next = temp
                self.tail.next = temp
                self.tail = temp

        # nodes in the posting list 
        class Node:
            def __init__(self, docID):
                self.docID = docID
                self.tf = 1
                self.next = None


    def initialize(self):
        with open(self.FILENAME) as file:
            seen = {}
            for line in file:
                line = line.lower()
                check = re.search('<doc id="(.*?)" url="(.*?)" title="(.*?)">', line)
                if check:
                    # 0 -> entire string, 1 -> id, 2 -> url, 3 -> title
                    seen = {}
                    self.docs[int(check[1])] = check[3]
                    current_doc = int(check[1])
                    continue
                    
                if line == '\n' or line == '</doc>\n':
                    continue
                
                # cleaning the line 
                line = re.sub('<a.*?>|</a>', '', line)
                line = re.sub('-|–|—', ' ', line)
                line = line.translate(str.maketrans("","", string.punctuation))

                # for every word encountered in document, add it to posting list 
                for term in line.strip().split(' '):
                    if term in self.InvertedIndex.keys():
                        self.InvertedIndex[term][0].add(current_doc)
                    else:
                        self.InvertedIndex[term] = [self.PostingList(current_doc), 0]

                    if not term in seen.keys():
                        seen[term] = 1
                        self.InvertedIndex[term][1] += 1
                    else:
                        seen[term] += 1

                # magnitude of (1+log(tf)) vector for each document 
                self.magnitude[current_doc] = np.linalg.norm(np.array(list(map(lambda x : (1+math.log2(x)) ,seen.values()))))

        self.no_documents = len(self.docs)