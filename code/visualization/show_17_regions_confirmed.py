from pandas import read_csv
from matplotlib import pyplot
data = read_csv('../../data/korea/covid/TimeProvince.csv', header=0, index_col=0)

# get 17 provinces
provinces = data['province'].unique()

df_pivoted = data.pivot(columns='province', values='confirmed')
df_begin = df_pivoted.iloc[[0]].reset_index().drop(['date'], axis=1)
df_end = df_pivoted.iloc[[-1]].reset_index().drop(['date'], axis=1)
df_end_sub_begin = df_end.sub(df_begin, axis='index')

# # For each province
# for province in provinces:
# 	# prepare situation
# 	X = data.loc[data['province'] == province]
# 	X = X['confirmed']
# 	window = 3
# 	history = [X[i] for i in range(window)]
# 	test = [X[i] for i in range(window, len(X))]
# 	predictions = list()
#

# plot
pyplot.title("province")
pyplot.plot(df_pivoted)
# pyplot.plot(predictions, color='red')
pyplot.savefig(f'../prediction/output_test/17_province_confirmed.png')
pyplot.close()
pyplot.show()
