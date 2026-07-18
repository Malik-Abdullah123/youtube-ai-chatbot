from flask import Flask, render_template, request, jsonify
from utils.rag import load_video, ask_question

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/load_video", methods=["POST"])
def load():

    video_id = request.json["video_id"]

    try:
        load_video(video_id)
        return jsonify({"status":"success"})
    except Exception as e:
        return jsonify({"status":"error","message":str(e)})


@app.route("/chat", methods=["POST"])
def chat():

    question=request.json["message"]

    answer=ask_question(question)

    return jsonify({"answer":answer})


if __name__=="__main__":
    app.run(debug=True)