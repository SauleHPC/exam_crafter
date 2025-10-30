from html_formatter import table_format_html, question_format_html
from sql_crafter  import sql_queries_problem
import json

from flask import Flask, jsonify, render_template

app = Flask(__name__)

def sql_query():
    my_problem = sql_queries_problem("")
    
    my_problem['tables_html'] = table_format_html(my_problem['tables'])
    my_problem['sql_basic_html'] = question_format_html(my_problem['sql_basic'])
    my_problem['sql_join_html'] = question_format_html(my_problem['sql_join'])
    my_problem['sql_groupby_html'] = question_format_html(my_problem['sql_groupby'])

    return my_problem

@app.route('/api/sql_query')
def sql_query_route():
    return jsonify(sql_query())

@app.route('/sql_query')
def sql_query_html():
    problem = sql_query()

    return render_template('sql_query.html',
                           tables_html = problem['tables_html'],
                           sql_basic_html = problem['sql_basic_html'],
                           sql_join_html = problem['sql_join_html'],
                           sql_groupby_html = problem['sql_groupby_html'])

    

#print(json.dumps(sql_query(), indent=1))
