from nltk.tokenize import sent_tokenize
import pickle

def inference(text_input, vectorizer, model):
    sentences = sent_tokenize(text_input)
    vectors = vectorizer.transform(sentences)
    scores = model.predict(vectors).round(2)
    formality = ["Formal" if score >= 0 else "Informal" for score in scores]
    return sentences, scores.tolist(), formality
    
def load_models(model_path, vec_path):
    model = pickle.load(open(model_path, 'rb'))
    vec = pickle.load(open(vec_path, 'rb'))
    return model, vec