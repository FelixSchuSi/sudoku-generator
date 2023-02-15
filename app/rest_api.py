from io import StringIO
import sys
from flask import Flask, request, jsonify, send_from_directory
from sudoku_grover import main

app = Flask(__name__, static_folder="static")


@app.route("/", methods=["POST"])
def index():
    buffer = StringIO()
    sys.stdout = buffer
    data = request.json
    print("Request: ", data)
    solved_sudoku, qasm = main(request_payload=data)
    result =  jsonify({"solved_sudoku": solved_sudoku.tolist(), "qasm": qasm, "logs": buffer.getvalue()})
    sys.stdout = sys.__stdout__
    return result


@app.route("/", methods=["GET"])
def frontend_html():
    return app.send_static_file("index.html")

@app.route('/<path:path>', methods=["GET"])
def frontend_js(path):
    return send_from_directory('static', path)

def entrypoint():
    return app
