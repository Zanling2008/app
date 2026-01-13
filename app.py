from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dữ liệu cảm xúc & biện pháp
EMOTION_DATA = {
    "vui": [
        "Tiếp tục duy trì những hoạt động tích cực bạn đang làm",
        "Chia sẻ niềm vui với bạn bè hoặc người thân",
        "Ghi lại khoảnh khắc tích cực trong nhật ký"
    ],
    "buon": [
        "Cho phép bản thân được nghỉ ngơi và thư giãn",
        "Tâm sự với người bạn tin tưởng",
        "Nghe nhạc nhẹ hoặc đi bộ"
    ],
    "tuc_gian": [
        "Hít thở sâu trong 1–2 phút",
        "Tạm rời khỏi tình huống gây tức giận",
        "Viết ra điều khiến bạn khó chịu"
    ],
    "lo_lang": [
        "Hít thở sâu theo nhịp 4-4",
        "Chia nhỏ vấn đề để giải quyết từng bước",
        "Tránh suy nghĩ quá xa trong tương lai"
    ],
    "cang_thang": [
        "Nghe nhạc thư giãn hoặc giãn cơ",
        "Ngủ đủ giấc và uống đủ nước",
        "Sắp xếp lại công việc theo mức độ ưu tiên"
    ]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotion", methods=["POST"])
def get_solution():
    emotion = request.json.get("emotion")
    solutions = EMOTION_DATA.get(emotion, [])
    return jsonify({"solutions": solutions})

if __name__ == "__main__":
    app.run(debug=True)
