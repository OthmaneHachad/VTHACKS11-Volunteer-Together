from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../volunteer-together-app/public')

@app.route('/<path:path>')
def static_file(path):
    try:
        return send_from_directory(app.static_folder, path)
    except:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
