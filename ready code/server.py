from flask import Flask, jsonify, request

app = Flask(__name__)

# Хранение состояния
door_status = {
    'room1': 'closed',
    'room2': 'open',
    'hallway': 'closed'
}

alarm_status = {
    'room1': 'off',
    'room2': 'on',
    'hallway': 'off'
}

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({'doors': door_status, 'alarm': alarm_status})

@app.route('/update_door/<room>', methods=['POST'])
def update_door(room):
    status = request.json.get('status')
    if room in door_status and status in ['open', 'closed']:
        door_status[room] = status
        return jsonify({'message': 'Status updated'}), 200
    return jsonify({'message': 'Invalid room or status'}), 400

@app.route('/update_alarm', methods=['POST'])
def update_alarm():
    global alarm_status
    status = request.json.get('status')
    if status in ['on', 'off']:
        alarm_status[status] = status
        return jsonify({'message': 'Alarm status updated'}), 200
    return jsonify({'message': 'Invalid status'}), 400

@app.route('/check_door/<room>', methods=['GET'])
def check_door(room):
    if room in door_status:
        return jsonify({'status': door_status[room]}), 200
    return jsonify({'message': 'Invalid room'}), 400

@app.route('/create_fire/<location>', methods=['POST'])
def create_fire(location):
    if location in alarm_status:
        if alarm_status[location] == 'on':
            return jsonify({'message': "Покидаем здание!! Скоро потушат помещение!"}), 200
        else:
            return jsonify({'message': "Это здание не будет подлежать восстановлению!"}), 200
    return jsonify({'message': 'Invalid location'}), 400

if __name__ == '__main__':
    app.run(debug=True)