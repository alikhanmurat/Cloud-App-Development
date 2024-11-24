const apiKey = '541fc6a686ed609076d0918583bab1fa'; 
const baseUrl = 'https://api.openweathermap.org/data/2.5/weather';

export const getWeatherData = async (city) => {
    const url = `${baseUrl}?q=${city}&appid=${apiKey}&units=metric`;
    const response = await fetch(url);
    return response.json();
};
