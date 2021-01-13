from flask import Flask, redirect, url_for, render_template, jsonify
import boto3

dynamo_client = boto3.client('dynamodb',region_name='us-east-2')
app = Flask(__name__)

def get_games():
    return dynamo_client.scan(
	TableName='HokieFootball'
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-games-db")
def db_games():
    return jsonify(get_games())
	

@app.route("/gameday")
def gameday():
    return render_template("gameday.html", games=["NC State", "Duke", "UNC", "Boston College", "Wake Forest", "Louisville", "Liberty", "Miami", "Pitt", "Clemson", "UVA"])

@app.route("/winning")
def winning():
    return render_template("result.html", results=["VT beat NC State 45-24", "VT beat Duke 38-31", "VT lost to UNC 45-56", "VT beat BC 40-14", "VT lost to WF 16-23", "VT beat UL 42-35", "VT lost to LU 35-38", "VT lost to Miami 24-25", "VT lost to Pitt 14-47", "VT loses to Clemson"])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
