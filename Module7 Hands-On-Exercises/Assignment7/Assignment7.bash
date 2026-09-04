read -r line < "SecretKey.txt"
curl -X GET "https://api.openweathermap.org/data/4.0/onecall/current?lat=52.2297&lon=21.0122&units=metric&lang=en&appid=$line" 