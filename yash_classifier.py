import pickle
import nltk

f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

test_predict = [classifier_tot.classify(t) for (t,s) in v_test]
