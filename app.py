import os
from flask import Flask, send_from_directory
from flask_cors import CORS
app = Flask(__name__, static_folder="./frontend/build")
CORS(app)
@app.route("/api/file/<path:filename>", methods=['GET'])
def openFile(filename):
    print("opening file")
    print(filename)
    file = open("content/test.md", 'r') 
    print(file)
    return file.read()
@app.route("/api/file", methods=['POST'])
def saveFile():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect("/")

@app.route('/', defaults={'path': ''})
@app.route('/index.html')
@app.route('/<path:path>')
def serve(path):
    print("serve function called")
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)

