from keras.models import load_model
# import openai
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
        self.answers = pd.read_csv(f'{file_path}/Answer_100.csv')['A']

        with open(f'{file_path}/QnA_words_to_csv_1000.csv', 'r', newline='') as f:
            for i in csv.reader(f):
                self.words += i
        # openai.api_key = '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'
        # self.openai = openai

        
    def preprocess_user_input(self, question, words):
        bag = [0 for _ in range(len(words))]

        s_words = self.kiwi.tokenize(question)
        s_wrds = [token[0] for token in s_words]

        for se in s_wrds:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
        
        return np.array([bag])
        
    def receive_answer(self, question):
        processed_input = self.preprocess_user_input(question, self.words)
        result = self.model.predict(processed_input)
        results_index = np.argmax(result)
        response = self.answers[results_index]
        return response
    
    # def chatGPT_answer(self, question):
    #     response = self.openai.Completion.create(
    #         engine="text-davinci-003",
    #         prompt=question,
    #         temperature=0.7,
    #         max_tokens=150)
    #     return response.choices[0].text.strip()