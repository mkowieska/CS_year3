const apiKey = '8b8cf1902618a6ccd765eab7d3469ca2';
const currentWeatherUrl = 'https://api.openweathermap.org/data/2.5/weather';
const forecastUrl = 'https://api.openweathermap.org/data/2.5/forecast';

document.getElementById('fetch-weather').addEventListener('click', () => {
    const city = document.getElementById('city-input').value;
    if (city) {
        fetchCurrentWeather(city);
        fetchWeatherForecast(city);
    } else {
        alert('Please enter a city name.');
    }
});

function fetchCurrentWeather(city) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `${currentWeatherUrl}?q=${city}&appid=${apiKey}&units=metric`);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);
            displayCurrentWeather(data);
        } else {
            console.error('Error fetching current weather:', xhr.responseText);
        }
    };
    xhr.onerror = function () {
        console.error('Network error occurred while fetching current weather.');
    };
    xhr.send();
}

function fetchWeatherForecast(city) {
    fetch(`${forecastUrl}?q=${city}&appid=${apiKey}&units=metric`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error fetching weather forecast');
            }
            return response.json();
        })
        .then(data => {
            displayForecast(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function displayCurrentWeather(data) {
    const container = document.getElementById('current-weather');
    const iconUrl = `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`;
    container.innerHTML = `
        <img src="${iconUrl}" alt="Weather icon">
        <p>Temperature: ${data.main.temp}°C</p>
        <p>Weather: ${data.weather[0].description}</p>
        <p>Humidity: ${data.main.humidity}%</p>
    `;
}


function displayForecast(data) {
    const container = document.getElementById('forecast');
    container.innerHTML = '';
    data.list.forEach((forecast, index) => {
        if (index % 8 === 0) { // Co 8 indeksów (~24 godziny)
            const iconUrl = `https://openweathermap.org/img/wn/${forecast.weather[0].icon}@2x.png`;
            const div = document.createElement('div');
            div.className = 'forecast';
            div.innerHTML = `
                <img src="${iconUrl}" alt="Weather icon">
                <p><strong>${new Date(forecast.dt_txt).toLocaleDateString()}</strong></p>
                <p>Temp: ${forecast.main.temp}°C</p>
                <p>${forecast.weather[0].description}</p>
            `;
            container.appendChild(div);
        }
    });
}
