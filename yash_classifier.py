import pickle
import nltk
classifier = nltk.classify.NaiveBayesClassifier
f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

test_predict = [classifier.classify(t) for (t,s) in v_test]
