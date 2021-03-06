from sklearn import svm
import pickle
import all_parsers
'''
My modeler is taking all windows of whole dataset as one list as it does not matter which seq the window belong to for taining purposes
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
windowlen = 11
X, Y = all_parsers.no_PSSM_input(DB, windowlen)
model = svm.LinearSVC(max_iter = 10000, tol=0.0003).fit(X, Y)
with open('../models/no_PSSM_model', 'wb') as f:
    pickle.dump(model, f)