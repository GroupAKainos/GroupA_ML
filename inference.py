from nltk.tokenize import sent_tokenize
import pandas as pd
import numpy as np
import pickle

def inference(text_input, vectorizer, model):
    sentences = sent_tokenize(text_input)
    vectors = vectorizer.transform(sentences)
    scores = model.predict(vectors).round(2)
    return sentences, scores
    

def pred_to_df(sentences, scores):
    sentence_formality_df = pd.DataFrame(np.column_stack([sentences, scores]), columns = ['Sentence', 'Formality Score'])
    sentence_formality_df['Formality Score'] = pd.to_numeric(sentence_formality_df['Formality Score'])
    sentence_formality_df.loc[sentence_formality_df['Formality Score'] < 0, 'Formality'] = 'Informal'
    sentence_formality_df.loc[sentence_formality_df['Formality Score'] > 0, 'Formality'] = 'Formal'
    return sentence_formality_df

def load_models(model_path, vec_path):
    model = pickle.load(open(model_path, 'rb'))
    vec = pickle.load(open(vec_path, 'rb'))
    return model, vec