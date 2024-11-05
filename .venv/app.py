from flask import Flask, jsonify, request
import database as db
import processRawData as prd
import processData as pd
import getRecommendation as get
import numpy as np
from getRecommendationFreelancer import getRecommendationFreelancer as get2

app = Flask(__name__)

# Định nghĩa route cho API GET
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Xin chào từ Flask API!"})

# Định nghĩa route cho API POST
@app.route('/api/trainai', methods=['GET'])
def trainai():
    #db.getDatabase()
    prd.processRawData()
    pd.processData()
    return jsonify({"status": "ok"})

# Định nghĩa route cho API GET
@app.route('/api/recommend/<int:id>', methods=['GET'])
def recommend(id):
    result = get.getRecommend(id)
    result = [
        int(x) if isinstance(x, (np.int64, np.int32)) else float(x) if isinstance(x, (np.float64, np.float32)) else x
        for x in result]
    return jsonify({"result": result})

@app.route('/api/recommendFeelancer/<int:id>', methods=['GET'])
def recommendFeelancer(id):
    result = get2(id);
    result = [
        int(x) if isinstance(x, (np.int64, np.int32)) else float(x) if isinstance(x, (np.float64, np.float32)) else x
        for x in result]
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
