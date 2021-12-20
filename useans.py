import tensorflow as tf

import tensorflow_hub as hub
import numpy as np
import os
import re

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" #@param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
model1 = hub.load(module_url)

def embed(input):
  return model1(input)

def plot_similarity(labels, features, rotation):
  corr = np.inner(features, features)
  print(corr)

def run_and_plot(messages_):
  message_embeddings_ = embed(messages_)
  plot_similarity(messages_, message_embeddings_, 90)

age = [
       "It is an interpreted, full-fledged programming language that enables dynamic interactivity on websites when applied to an HTML document.",
       "Javascript is a functional programming language used to create dynamic web pages",
]

run_and_plot(age)