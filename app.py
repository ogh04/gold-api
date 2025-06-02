import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# تحميل الملفات الثلاثة من CSV
df1 = pd.read_csv('gold_data1.csv')
df2 = pd.read_csv('gold_data2.csv')
df3 = pd.read_csv('gold_data3.csv')

# نقاط النهاية لكل ملف CSV
@app.route('/api/gold1', methods=['GET'])
def get_gold1():
    return jsonify(df1.to_dict(orient='records'))

@app.route('/api/gold2', methods=['GET'])
def get_gold2():
    return jsonify(df2.to_dict(orient='records'))

@app.route('/api/gold3', methods=['GET'])
def get_gold3():
    return jsonify(df3.to_dict(orient='records'))

# نقطة نهاية ترجع كل الملفات مع بعض (اختياري)
@app.route('/api/gold', methods=['GET'])
def get_all_gold():
    return jsonify({
        'gold1': df1.to_dict(orient='records'),
        'gold2': df2.to_dict(orient='records'),
        'gold3': df3.to_dict(orient='records')
    })

if __name__ == '__main__':
    app.run(debug=True)







