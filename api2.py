from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import argparse
import numpy as np
from questiongenerator import QuestionGenerator
from questiongenerator import print_qa
import tensorflow_hub as hub

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('context', type=str, location=['form', 'args', 'values'])

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" #@param ["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
model1 = hub.load(module_url)

qg = QuestionGenerator()

js = "JavaScript (js) is a light-weight object-oriented programming language which is used by several websites for scripting the webpages. It is an interpreted, full-fledged programming language that enables dynamic interactivity on websites when applied to an HTML document. It was introduced in the year 1995 for adding programs to the webpages in the Netscape Navigator browser. Since then, it has been adopted by all other graphical web browsers. With JavaScript, users can build modern web applications to interact directly without reloading the page every time. The traditional website uses js to provide several forms of interactivity and simplicity."

with open('articles/owl_rescue.txt', 'r') as a:
    article = a.read()

class Question(Resource):
    def get(self):
        qa_list = qg.generate(
            js, 
            num_questions=1, 
            answer_style='sentences'
        )
        print_qa(qa_list)
        return {'q': qa_list}
    
    def post(self):
        args = parser.parse_args()
        context = args['context']
        print(context)
        qa_list = qg.generate(
            context, 
            num_questions=1, 
            answer_style='sentences'
        )
        print_qa(qa_list)
        return {'q': qa_list}, 200

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
class Answer(Resource):
    def get(self):
        run_and_plot(age)
        return {'q': "works"}

api.add_resource(Question, '/')
api.add_resource(Answer, '/ans')

if __name__ == '__main__':
    app.run(debug=True)