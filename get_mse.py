data = [(1, 3),
		(2, 5),]
m = -1
b = 5

def get_mse(data, m, b):
	n = len(data)
	squared_error = 0
	for x, y in data:
		y_hat = m*x+b
		squared_error += (y - y_hat) ** 2
	mse = squared_error / n
	return mse

print(get_mse(data, m, b))

