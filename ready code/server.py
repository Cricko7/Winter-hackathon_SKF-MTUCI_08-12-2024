import os
from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

# Хранение состояния
door_status = {
    'комната 1': 'closed',
    'комната 2': 'open',
    'коридор': 'closed'
}

alarm_status = {
    'комната 1': 'off',
    'комната 2': 'on',
    'коридор': 'off'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def get_status(): #Должно вернуть текущее состояние дверей
    return jsonify({'doors': door_status, 'alarm': alarm_status})

@app.route('/update_door/<room>', methods=['POST'])
def update_door(room):
    #Обновляет состояние двери.
    status = request.json.get('status')
    if room in door_status and status in ['open', 'closed']:
        door_status[room] = status
        return jsonify({'message': 'Статус двери обновлен'}), 200
    return jsonify({'message': 'Неверное название комнаты или статус'}), 400

@app.route('/update_alarm', methods=['POST'])
def update_alarm():
    #Обновляет состояние сигнализации.
    global alarm_status
    status = request.json.get('status')
    if status in ['on', 'off']:
        for room in alarm_status:
            alarm_status[room] = status
        return jsonify({'message': 'Статус сигнализации обновлен'}), 200
    return jsonify({'message': 'Неверный статус'}), 400

@app.route('/check_door/<room>', methods=['GET'])
def check_door(room):
    #Проверяет состояние двери.
    if room in door_status:
        return jsonify({'status': door_status[room]}), 200
    return jsonify({'message': 'Неверное название комнаты'}), 400

@app.route('/create_fire/<location>', methods=['POST'])
def create_fire(location): #Показывает место, где совершили пожар.
    if location in alarm_status:
        if alarm_status[location] == 'on':
            return jsonify({'message': "Покидаем здание!! Скоро потушат помещение!"}), 200
        else:
            return jsonify({'message': "Это здание не будет подлежать восстановлению!"}), 200
    return jsonify({'message': 'Неверное место'}), 400

if __name__ == "__main__":
    app.run()