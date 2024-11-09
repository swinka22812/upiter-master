from flask import Flask, request, jsonify

app = Flask(__name__)

# Статический список ключей и их привязка к HWID
valid_keys = {
    "test": "178BFBFF00870F10",  # Пример ключа и привязанного HWID
}

@app.route('/api/auth', methods=['GET'])
def authenticate():
    """
    Проверяет ключ пользователя и его HWID.
    """
    auth_key = request.args.get('auth_key')  # Получаем ключ из параметров URL
    hwid = request.args.get('hwid')  # Получаем HWID из параметров URL

    # Проверяем, есть ли такой ключ и привязан ли он к правильному HWID
    if auth_key in valid_keys and valid_keys[auth_key] == hwid:
        return jsonify({"success": True}), 200  # Успех
    else:
        return jsonify({"success": False}), 401  # Ошибка аутентификации

if __name__ == '__main__':
    app.run(debug=True)
