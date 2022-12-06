from api.api_inference import inference, load_models
import json

model_path = "./models/model.pkl"
vec_path = "./models/vec.pkl"

model, vec = load_models(model_path, vec_path)

def lambda_handler(event, context):
    text = event['body']
    print("Input text:", text, type(text))

    sentences, scores, formality = inference(text, vec, model)

    print("Sentences:", sentences)  
    print("Scores:", scores)
    print("Formality:", formality)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "sentences": sentences,
                "scores": scores,
                "formality": formality

            }
        )
    }
