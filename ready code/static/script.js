async function fetchStatus() {
    const response = await fetch('/status');
    const data = await response.json();
    
    document.getElementById('door-status').innerText = JSON.stringify(data.doors);
    document.getElementById('alarm-status').innerText = data.alarm ? 'Сигнализация включена' : 'Сигнализация выключена';
}

setInterval(fetchStatus, 5000); // Обновление статуса каждые 5 секунд