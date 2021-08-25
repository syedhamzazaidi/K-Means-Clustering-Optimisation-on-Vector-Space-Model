# K-Means-Clustering-Optimisation-on-Vector-Space-Model
K Means Clustering Optimisation on a Vector Space Model of a subset of the wikipedia dataset. This was done as a capstone project for the course CS F469 Information Retrieval at BITS Pilani.

Installing dependencies:
``` 
pip install -r requirements.txt
```

All the parts have their code in their individual python notebooks. The instructions to run the code and context are written in the notebooks themselves.

Open and run the notebook in the following order:

Part 1A : "Part 1A - Vector Space Model.ipynb"  
Part 1B : "Part 1B - Test Queries.ipynb"  
Part 2A.1 : "Part2A_index.ipynb"   
Part 2A.2 : "part2A_search.ipynb"  
Part 2B : "Part 2B - KMeans Clustering.ipynb"  

---

### Notes: 
- Part 1B and 2B both require 'vector_space_model.csv' file which is generated in Part 1A
- Part 2A.2 will require 'inverted_index_obj.pickle' file which is generated in Part 2A.1
- Part 1A and 2A.1 will require a single 'wiki' file. The easiest way to do this would be to put the file in the same directory as the notebooks and enter the name of the file when asked for the path.
- The notebooks have been tested on only a subset of the corpus provided. For guaranteed results, please run file 'AN/wiki_93' or 'AN/wiki_91'
