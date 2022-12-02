import plotly.express as px
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def scatter(df_test, Y_pred):
    df_test['predictions'] = Y_pred.tolist()
    fig = px.scatter(df_test, x = 'predictions', y = 'avg_score',
                    labels={'predictions':'Predicted', 'avg_score':'Ground Truth'},
                    title="Ground truth vs Predicted"
                    )
    fig.add_shape(type='line',
                    x0=-3,
                    y0=-3,
                    x1=3,
                    y1=3,
                    line=dict(color='Red',),
                    xref='x',
                    yref='y'
    )
    fig.show("png")

def sent_len_formality(df_test, Y_pred):
    df_test['predictions'] = Y_pred.tolist()
    df_test['sentence_length_char'] = df_test['sentence'].str.len()
    df_test['sentence_length_words'] = df_test['sentence'].str.split().str.len()
    df_test['avg_word_length'] = df_test['sentence_length_char']/df_test['sentence_length_words']

    #ground truth corr matrix
    fig = px.imshow(df_test[['avg_score', 'sentence_length_char', 'sentence_length_words', 'avg_word_length']].corr(),
                   title="Ground Truth Correlation Matrix",
                   text_auto=True
               )
    fig.show("png")

    #predicted corr matrix
    fig = px.imshow(df_test[['predictions', 'sentence_length_char', 'sentence_length_words', 'avg_word_length']].corr(),
                   title="Predictions Correlation Matrix",
                   text_auto=True
               )
    fig.show("png")

    #ground truth heatmap
    fig = px.density_heatmap(df_test, x='sentence_length_words', y='avg_score',
                         labels={'avg_score':'Formality score', 'sentence_length_words':'Number of Words', 'sentence_length_char':'Number of characters'},
                         title="Density Heatmap of ground truth formality scores vs number of words in sentence"
                        )
    fig.show("png")

    #predicted heatmap
    fig = px.density_heatmap(df_test, x='sentence_length_words', y='predictions',
                         labels={'avg_score':'Formality score', 'sentence_length_words':'Number of Words', 'sentence_length_char':'Number of characters'},
                         title="Density Heatmap of predicted formality scores vs number of words in sentence"
                        )
    fig.show("png")

def formality_of_features(model, vectorizer):
    features = vectorizer.get_feature_names_out()
    ascending_ind = np.argsort(model.coef_)
    
    print("Features that influence an informal score the most:")
    print(*features[ascending_ind[:10]], sep =', ')
    print("\n")
    print("Features that influence a formal score the most:")
    print(*features[ascending_ind[-10:]], sep =', ')
    print("\n")

    print("Informal WordCloud:")
    wordcloud = WordCloud().generate(" ".join(features[ascending_ind[:100]]))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    print("Formal WordCloud:")
    wordcloud = WordCloud().generate(" ".join(features[ascending_ind[-100:]]))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()