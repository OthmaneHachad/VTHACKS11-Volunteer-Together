from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../volunteer-together-app/public')

@app.route('/')
def serve():
    # serving the svelte app
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_file(path):
    # serving any sub pages of the svelte app
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
