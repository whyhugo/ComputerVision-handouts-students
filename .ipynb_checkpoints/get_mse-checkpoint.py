x1 = 1
y1 = 3
x2 = 2
y2 = 5

date = [(x1, y1),(x2, y2)]
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

