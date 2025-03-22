# tests/fixtures/sample_transcripts.py
"""
Sample transcripts for testing the YouTube Transcript Analyzer
"""

SHORT_TRANSCRIPT = """
Hello and welcome to this tutorial on Python programming.
Today we'll be covering the basics of Python syntax and how to get started.
First, let's talk about variables. In Python, you don't need to declare variable types.
Next, we'll look at control structures like if statements and loops.
Finally, we'll discuss functions and how to create them in Python.
"""

MEDIUM_TRANSCRIPT = """
Welcome to this in-depth tutorial on machine learning with TensorFlow.
In this video, we'll cover the basics of machine learning, neural networks, and how to implement them using TensorFlow.

First, let's discuss what machine learning is. Machine learning is a subset of artificial intelligence that allows computers to learn from data without being explicitly programmed.

There are several types of machine learning:
1. Supervised learning
2. Unsupervised learning
3. Reinforcement learning

For this tutorial, we'll focus on supervised learning, which involves training a model on labeled data.

Next, let's talk about neural networks. Neural networks are a powerful machine learning technique inspired by the human brain.

Now, let's set up our TensorFlow environment and write some code.
First, we need to import the necessary libraries:
import tensorflow as tf
import numpy as np

Then, we'll create a simple neural network model:
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(10, activation='relu', input_shape=(8,)))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

Finally, we'll compile and train our model:
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)

That's it for this tutorial. In the next video, we'll explore more advanced techniques.
"""

# Add more sample transcripts as needed