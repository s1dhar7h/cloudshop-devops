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

@app.route("/users")
def users():
    return jsonify({
        "users": [
            {
                "ID":1,
                "Name":"Sidharth"
            },
            {
                "ID":2,
                "Name":"Muraleedharan"
            }
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)