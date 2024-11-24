import React, { useState } from 'react';
import { getWeatherData } from './maincode';

function App() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);

  const fetchWeather = async () => {
    const data = await getWeatherData(city);
    setWeather(data);
  };

  return (
    <div className="App">
      <h1>Weather Dashboard</h1>
      <input
        type="text"
        placeholder="Enter city"
        onChange={(e) => setCity(e.target.value)}
      />
      <button onClick={fetchWeather}>Get Weather</button>

      {weather && (
        <div>
          <h2>{weather.name}</h2>
          <p>{weather.weather[0].description}</p>
          <p>{weather.main.temp} °C</p>
        </div>
      )}
    </div>
  );
}

export default App;
