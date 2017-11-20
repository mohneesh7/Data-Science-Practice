from sklearn import datasets
from sklearn.datasets import make_regression,make_blobs,make_classification
import matplotlib.pyplot as plt
import pandas as pd

def load_iris():
	iris = datasets.load_iris()

	# load data 
	X = iris.data

	# create target vector
	Y = iris.target
	print Y

	# plot the different datasets
	plt.scatter(X[:,0],X[:,1],X[:,2])
	plt.show()

def regression_simulate():
	features,output,coef = make_regression(n_samples = 100,
										   # three features
										   n_features = 3,
										   # where only two features are useful
										   n_informative=2,
										   # a single target value per observation
										   n_targets=1,
										   # show the true coefficient used to generate the data
										   coef=True)
	a= pd.DataFrame(features,columns =['a','b','c']).head()
	b = pd.DataFrame(output).head()
	print a,"\n",b

def cluster_simulate():
	X,y = make_blobs(n_samples = 200,
					 # two feature variables
					 n_features = 2,
					 # three clusters
					 centers = 3,
					 # cluster_standard deviation
					 cluster_std =0.5,
					 # shuffled
					 shuffle = True)
	plt.scatter(X[:,0],X[:,1])
	plt.show()

def classification_simulate():
	features,output = make_classification(n_samples = 200,
										  n_features = 5,
										  n_informative = 2,
										  n_redundant = 3,
										  # number of classes
										  n_classes = 2,
										  # with 20% observation in the first class 30% in the second and 50% in the third
										  weights = [.5,.5])
	a = pd.DataFrame(features).head()
	b = pd.DataFrame(output).head()

