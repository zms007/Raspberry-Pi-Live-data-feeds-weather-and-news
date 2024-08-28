from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace with your own API keys
WEATHER_API_KEY = '9048cf3bf58b51594f687aed86326f02'
NEWS_API_KEY = '9c3213430de14a518544f74248ec2428'

# Replace with your desired location
LOCATION = 'Kuala Lumpur'

def get_weather():
    # Example API call for weather data
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={WEATHER_API_KEY}&units=metric'
    weather_data = requests.get(weather_url).json()
    return f"{weather_data['name']}: {weather_data['main']['temp']}°C, {weather_data['weather'][0]['description']}"

def get_news():
    # Example API call for news data
    news_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    news_data = requests.get(news_url).json()
    headlines = [article['title'] for article in news_data['articles'][:5]]
    return headlines

@app.route('/')
def index():
    weather = get_weather()
    news = get_news()
    return render_template('index.html', weather=weather, news=news)

if __name__ == '__main__':
    app.run(debug=True)
