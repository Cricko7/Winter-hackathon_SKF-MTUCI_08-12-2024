async function fetchStatus() {
    const response = await fetch('/status');
    const data = await response.json();
    
    document.getElementById('door-status').innerText = JSON.stringify(data.doors);
    document.getElementById('alarm-status').innerText = data.alarm.room1 === 'on' ? 
        'Сигнализация включена в комнате 1' : 
        (data.alarm.room2 === 'on' ? 
            'Сигнализация включена в комнате 2' : 
            (data.alarm.hallway === 'on' ? 
                'Сигнализация включена в коридоре' : 
                'Сигнализация выключена'));
}

async function updateDoor(room, status) {
    const response = await fetch(`/update_door/${room}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status })
    });
    
    const result = await response.json();
    alert(result.message);
    
    fetchStatus(); // Обновляем статус после изменения
}

async function updateAlarm(status) {
    const response = await fetch('/update_alarm', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status })
    });
    
    const result = await response.json();
    alert(result.message);
    
    fetchStatus(); // Обновляем статус после изменения
}

// Обновление статуса при загрузке страницы
fetchStatus();