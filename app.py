from html_formatter import table_format_html, question_format_html
from sql_crafter  import sql_queries_problem
import json
import theme
    
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def sql_query():
    mytheme = theme.theme_selector()['theme_selected']
    
    my_problem = sql_queries_problem(mytheme)
    
    return my_problem

@app.route('/api/sql_query')
def sql_query_route():
    return jsonify(sql_query())

@app.route('/sql_query')
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
