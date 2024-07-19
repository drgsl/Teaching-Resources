# Multilayer Perceptron (MLP) for Iris Flower Classification

This is a Python script for training and testing a Multilayer Perceptron (MLP) on the Iris flower dataset. The MLP is implemented from scratch using NumPy and Matplotlib libraries.

## Dependencies
- Python 3.x
- NumPy
- Matplotlib

## Parameters
The following parameters can be modified in the script:

- `EPOCH`: number of training epochs.
- `LEARNING_RATE`: learning rate used in the backpropagation algorithm.
- `BATCH_SIZE`: size of each batch used in the training.
- `MOMENTUM`: momentum used in the backpropagation algorithm.
- `L2`: L2 regularization term used in the weight update.

## Overview

- The code is implementing a neural network with one hidden layer to classify the iris dataset.
- The code reads the data from a file, 
- shuffles the data, 
- and splits it into train and test sets. 
- It then defines the parameters for the neural network, 
  -such as the number of hidden units, 
  - learning rate, 
  - and batch size. 
  - The weights and biases for the neural network are initialized randomly. 
- The sigmoid, sigmoid_derivative, and softmax activation functions are defined. 
- The feedforward function is defined to compute the output of the neural network for a given input. 

- The backpropagation function is defined to compute the gradients of the weights and biases with respect to the loss function. 
- The train function is defined to train the neural network using stochastic gradient descent with momentum and L2 regularization.
