new Chart(document.getElementById('airChart'), {
    type: 'line',
    data: {
        labels: air_labels,
        datasets: [{
            label: 'AQI Trend',
            data: air_values,
            borderWidth: 3,
            tension: 0.45,
            fill: false
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: true }
        }
    }
});

new Chart(document.getElementById('waterChart'), {
    type: 'line',
    data: {
        labels: water_labels,
        datasets: [{
            label: 'pH Level',
            data: water_values,
            borderWidth: 3,
            tension: 0.45,
            fill: false
        }]
    },
    options: {
        responsive: true
    }
});
