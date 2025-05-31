import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


df1 = pd.read_csv('gold_data1.csv')
df2 = pd.read_csv('gold_data2.csv')
df3 = pd.read_csv('gold_data3.csv')

df = pd.concat([df1, df2, df3], ignore_index=True)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

@app.route('/api/gold', methods=['GET'])
def get_gold_data():
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True) 









