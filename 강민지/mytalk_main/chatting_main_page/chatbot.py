from keras.models import load_model
import numpy as np
import pandas as pd
import numpy as np
from kiwipiepy import Kiwi
import pandas as pd
import csv
import os

class Chatbot():
    def __init__(self):
        file_path = f'{os.getcwd()}/static/chatbot_data'
        self.words = []
        self.kiwi = Kiwi()
        self.model = load_model(f'{file_path}/QnA_keras_model_1000.h5')
        self.answers = pd.read_csv(f'{file_path}/Q&A.csv').head(1000)['A']

        with open(f'{file_path}/QnA_words_to_csv_1000.csv', 'r', newline='') as f:
            for i in csv.reader(f):
                self.words += i   
        
    def preprocess_user_input(self, question):
        s_words = self.kiwi.tokenize(question)
        s_wrds = [token[0] for token in s_words]
        bag = [1 if w in s_wrds else 0 for w in self.words]
        return bag
        
    def receive_answer(self, question):
        processed_input = self.preprocess_user_input(question)
        result = self.model.predict(np.array([processed_input]))
        results_index = np.argmax(result)
        response = self.answers[results_index]
        return response

