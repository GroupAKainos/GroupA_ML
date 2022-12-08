# Formality classification tool with AWS Endpoint

Produce a tool that will determine the formality of a job description and highlight any informal sentences that may need to be amended.

The tool takes as input a paragraph of test and outputs the formality score for each sentence. Positive scores relate to a formal classification and negative scores relate to a informal classification.

## Download

To enable the notebooks to run, please download the following .csv files from [here](https://huggingface.co/datasets/osyvokon/pavlick-formality-scores/tree/main) and save them in ./data (Hint: click on the file size):
- all.csv
- test.csv
- train.csv

### AWS Endpoint

The AWS Endpoint is located at the following url:
- https://i9ie7dtl73.execute-api.eu-west-2.amazonaws.com/Prod/formality-score/