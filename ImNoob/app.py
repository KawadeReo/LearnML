from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def parse_command(command):
    """
    コマンド解析の簡単なサンプル関数です。
    例として、「検索」または「search」が含まれる場合、検索タスクとして処理します。
    """
    if "検索" in command or "search" in command:
        # 「検索」で区切る（シンプルな実装例）
        query = command.split("検索")[-1].strip() if "検索" in command else command.split("search")[-1].strip()
        result = f"【検索結果】「{query}」に関する情報を取得しました。"
    else:
        result = f"【実行結果】コマンド「{command}」を実行しました。"
    return result

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    command = data.get("command", "")
    result = parse_command(command)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
