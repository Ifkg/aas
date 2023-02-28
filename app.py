from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘀𝗼𝘂𝗿𝗰𝗲 𝗮𝗯𝗼𝗱'


if __name__ == "__main__":
    app.run()
