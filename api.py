from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import argparse
import numpy as np
from questiongenerator import QuestionGenerator
from questiongenerator import print_qa

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('context', type=str, location=['form', 'args', 'values'])
parser.add_argument('qnos', type=int, location=['form', 'args', 'values'])

qg = QuestionGenerator()

js = "Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples that we provide. The primary aim is to allow the computers learn automatically without human intervention or assistance and adjust actions accordingly.But,using the classic algorithms of machine learning, text is considered as a sequence of keywords; instead, an approach based on semantic analysis mimics the human ability to understand the meaning of a text."
class Question(Resource):
    def get(self):
        qa_list = qg.generate(
            js, 
            num_questions=1, 
            answer_style='sentences'
        )
        # print_qa(qa_list)
        return {'q': qa_list}
    
    def post(self):
        args = parser.parse_args()
        context = args['context']
        qnos = args['qnos']
        # print(context)
        qa_list = qg.generate(
            context, 
            num_questions=qnos, 
            answer_style='sentences'
        )
        # print_qa(qa_list)
        return {'q': qa_list}, 200

api.add_resource(Question, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)