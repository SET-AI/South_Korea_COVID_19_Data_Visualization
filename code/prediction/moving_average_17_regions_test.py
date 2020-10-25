from pandas import read_csv
from numpy import mean
from sklearn.metrics import mean_absolute_error
from matplotlib import pyplot
data = read_csv('../../data/korea/covid/TimeProvince.csv', header=0, index_col=0)

# get 17 provinces
provinces = data['province'].unique()

# For each province
for province in provinces:
	# prepare situation
	X = data.loc[data['province'] == province]
	X = X['confirmed']
	window = 3
	history = [X[i] for i in range(window)]
	test = [X[i] for i in range(window, len(X))]
	predictions = list()

	# walk forward over time steps in test
	for t in range(len(test)):
		length = len(history)
		yhat = mean([history[i] for i in range(length-window,length)])
		obs = test[t]
		predictions.append(yhat)
		history.append(obs)
		# print('predicted=%f, expected=%f' % (yhat, obs))

	error = mean_absolute_error(test, predictions)
	print(f'{province}\t%.3f' % error)

	# plot
	pyplot.title(province)
	pyplot.plot(test)
	pyplot.plot(predictions, color='red')
	pyplot.savefig(f'output_test/{province}.png')
	pyplot.close()
	pyplot.show()
