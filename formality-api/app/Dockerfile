FROM public.ecr.aws/lambda/python:3.9

COPY app.py ./
COPY requirements.txt ./
COPY api ./api/
COPY models/* ./models/

RUN python3.9 -m pip install -r requirements.txt -t .
RUN mkdir -p /var/lang/nltk_data
RUN python3.9 -c "import nltk; a = [nltk.download(_, download_dir='/var/lang/nltk_data') for _ in ['punkt']]"

CMD ["app.lambda_handler"]
