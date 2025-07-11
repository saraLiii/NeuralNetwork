import numpy as np


class MyPerceptron:
    """
    MyPerceptron 我的感知机
    调整了一下predict函数，不仅仅是分类而是计算出某一个具体的值
    """
    def __init__(self, input_dim, lr=0.1, epoch=100, bias=0):
        self.w = np.zeros(input_dim)
        self.b = bias
        self.lr = lr
        self.epoch = epoch
        self.threshold = 0

    def activation(self, value):
        return 1 if value >= self.threshold else 0

    def predict(self, x):
        return np.dot(x, self.w) + self.b

    def learning(self, X, y):
        for epoch in range(self.epoch):
            errors = 0  # loss function
            for xi, yi in zip(X, y):
                prediction = self.predict(xi)
                error = yi - prediction
                self.w += self.lr * error * xi
                self.b += self.lr * error
                if error != 0:
                    errors += 1
            if errors == 0:
                print(f"Converged after {epoch + 1} iterations.")
                print("Stopping criteria")
                break

    def print_weights(self):
        print(f"weight:{self.w}, bias:{self.b}")


X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
And_Y = np.array([0, 0, 0, 1])
Or_Y = np.array([0, 1, 1, 1])
Xor_Y = np.array([0, 1, 1, 0])
axb_Y = np.array([1, 0, 1, 0])


def test_perceptron(X, Y):
    perceptron = MyPerceptron(input_dim=2)
    perceptron.learning(X, Y)
    perceptron.print_weights()
    for xi, yi in zip(X, Y):
        prediction = perceptron.predict(xi)
        print(f"Input: {xi}, Prediction: {prediction}, Target: {yi}")


if __name__ == "__main__":
    test_perceptron(X, axb_Y)

