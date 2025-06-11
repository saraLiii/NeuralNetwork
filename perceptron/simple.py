import numpy as np

class Perceptron:
    def __init__(self, input_dim,lr=0.1,epoch=100,bias=0):
        self.w = np.zeros(input_dim)
        self.b=bias
        self.lr = lr
        self.epoch = epoch
        self.threshold = 0

    def activation(self, value):
        return 1 if value >= self.threshold else 0


    def predict(self,x):
        return self.activation(np.dot(x,self.w)+self.b)


    def learning(self, X, y):
        for epoch in range(self.epoch):
            errors = 0   #   loss function
            for xi,yi in zip(X,y):
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
And_Y=np.array([0,0,0,1])
Or_Y=np.array([0,1,1,1])
Xor_Y=np.array([0,1,1,0])

def test_perceptron(X,Y):
    perceptron = Perceptron(input_dim=2)
    perceptron.learning(X,Y)
    perceptron.print_weights()


if __name__ == "__main__":
    test_perceptron(X,Xor_Y)

