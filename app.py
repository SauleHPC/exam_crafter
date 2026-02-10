from html_formatter import table_format_html, question_format_html
import sql_crafter
import json
import theme
import config
import db

from flask import Flask, jsonify, render_template, request, abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for all HTTP errors."""
    # Start with the correct headers and status code from the error
    response = e.get_response()
    # Replace the body with JSON
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }).data
    response.content_type = "application/json"
    return response


def sql_query():
    mytheme = theme.theme_selector()['theme_selected']
    
    my_problem = sql_crafter.sql_queries_problem(mytheme)
    
    return my_problem

@app.route('/api/gen_sql_query')
def sql_query_route():
    return jsonify(sql_query())

def check_secret():
    data = request.get_json()
    meta = None
    if not data:
        abort (400, description="Missing JSON in request")

    try:
        meta = data['meta']
        meta['secret'] #throws if secret undefined
    except KeyError as k:
        abort  (400, "malformed JSON")

    if meta['secret'] != config.config['me_as_backend']['secret']:
        abort (401, "no secret")

    
def load_payload():
    data = request.get_json()
    payload = None
    
    if not data:
        abort (400, description="Missing JSON in request")

    try:
        payload = data['payload']
        
    except KeyError as k:
        abort  (400, description="malformed JSON")
    
    return payload

@app.route('/api/upload_sql_query', methods=['POST'])
def upload_sql_query_route():
    check_secret()
    payload = load_payload()

    if not isinstance(payload, dict):
        abort (400, description="malformed payload")
    
    for k in payload:
        if not sql_crafter.validate_sql_problem(payload[k]):
            abort (400, f"malformed problem {k}")

        db.add_sql_problem(k, payload[k])
    
    return jsonify({"payload": payload}), 200


@app.route('/api/get_random_sql_query')
def get_random_sql_query_route():
    pb = db.get_random_sql_problem()

    return jsonify({"id": pb[0], "pb": pb[1]}), 200


@app.route('/api/get_sql_query', methods=['POST'])
def get_sql_query_route():
    check_secret()
    payload = load_payload()

    if not isinstance(payload, str):
        abort (400, description="malformed payload")

    my_id = payload
    pb = db.get_sql_problem(my_id)

    if pb == None:
        abort (404, f"Problem {my_id} not found")
    
    return jsonify({"id": pb[0], "pb": pb[1]}), 200
    



@app.route('/gen_sql_query')
def sql_query_html():
    problem = sql_query()

    return render_template('sql_query.html',
                           theme = problem['theme'],
                           tables = problem['tables'],
                           sql_basic = problem['sql_basic'],
                           sql_join = problem['sql_join'],
                           sql_groupby = problem['sql_groupby'])

@app.route('/api/theme')
def theme_route():
    return jsonify(theme.theme_selector())




#print(json.dumps(sql_query(), indent=1))
