import requests
from flask import Flask, jsonify,request

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    try:
        return "B0JfHwN2D9MEDkNttz/o41234n84hbD19TTVsI1/58XGS4RkmIumkFuVgbiLCtRxq67PqrO1K8XLhnP6OqR7xg=="
    except:
        return "e"

context = ('serf.crt', 'key.key')#cs
app.run(debug=True,host="0.0.0.0",port=443,ssl_context=context)
