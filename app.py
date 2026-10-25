from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Like API Running! Use /like?uid=YOUR_ID"

@app.route('/like')
def like():
    uid = request.args.get('uid')
    region = request.args.get('region', 'BD')
    if not uid:
        return jsonify({"error": "uid daw"}), 400
    return jsonify({
        "status": "success",
        "uid": uid,
        "region": region,
        "likes": 100,
        "message": f"100 Like sent to {uid}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)