from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "Service":"User Service",
        "Status":"Running"
    })

@app.route("/health")
def health():
    return jsonify({
        "Status":"Healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5004)