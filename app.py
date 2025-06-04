import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# تحميل ملف CSV الوحيد
df = pd.read_csv('million.csv')

# نقطة نهاية واحدة ترجع كل البيانات
@app.route('/api/gold', methods=['GET'])
def get_gold():
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)



