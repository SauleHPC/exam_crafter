# Exam Crafter

This is a repository that provides tools to help generate exams on a fixed format using LLMS.
At the time of writing, it only supports generating basic SQL query questions.

## Install

It's a python flask server.  There is a `requirements.txt` file. So
you can pip install the dependencies with:

```
pip install -r requirements.txt
```

## Run it

```
FLASK_APP=app.py flask run
```

This will start the server on localost port 5000 by default. Check Flask doc for customization.

### Configure LLM

This is configured to hit a CCI internal LLM. But this uses the
[aisuite](https://github.com/andrewyng/aisuite) python package to
abstract the llms. So you should be able to configure the LLM system
you want.

The configuration happens in `llm_provider.py`.

## Use it

It's gonna take a minute (like an actual minute) to answer most
queries the way the code is currently written. So be patient.

1. [An HTML formatted question](http://127.0.0.1:5000/sql_query)
2. [JSON of query](http://127.0.0.1:5000/api/sql_query)
3. [JSON of themes](http://127.0.0.1:5000/api/theme)

