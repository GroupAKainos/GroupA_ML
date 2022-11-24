# GroupA_ML

Produce a tool that will determine the formality of a job description and highlight any informal sentences that may need to be amended.


## Dataset (Pavlick Formality Scores)

Includes sentences from four genres (news, blogs, email, and QA forums), all annotated by humans on Amazon Mechanical Turk.

[Link](https://huggingface.co/datasets/osyvokon/pavlick-formality-scores) to Dataset on Huggingface.

**Contents**

The annotated data files and number of lines in each are as follows:
- 4977 answers -- Annotated sentences from a random sample of posts from the Yahoo! Answers forums: https://answers.yahoo.com/
- 1821 blog -- Annotated sentences from the top 100 blogs listed on http://technorati.com/ on October 31, 2009.
- 1701 email -- Annotated sentences from a random sample of emails from the Jeb Bush email archive: http://americanbridgepac.org/jeb-bushs-gubernatorial-email-archive/
- 2775 news -- Annotated sentences from the "breaking", "recent", and "local" news sections of the following 20 news sites: CNN, CBS News, ABC News, Reuters, BBC News Online, New York Times, Los Angeles Times, The Guardian (U.K.), Voice of America, Boston Globe, Chicago Tribune, San Francisco Chronicle, Times Online (U.K.), news.com.au, Xinhua, The Times of India, Seattle Post Intelligencer, Daily Mail, and Bloomberg L.P.

**Format**

Each record contains the following fields:
- domain: source of sentences
- avg_score: the mean formality rating, which ranges from -3 to 3 where lower scores indicate less formal sentences
- sentence

**Download**

To enable this notebook to run, please download the following .csv files  from [here](https://huggingface.co/datasets/osyvokon/pavlick-formality-scores/tree/main) and save them in ./data (Hint: click on the file size):
- all.csv
- test.csv
- train.csv