temperature = [32, 34, 33, 35, 36, 34, 33, 32, 31, 35]   
humidity = [45, 50, 55, 60, 58, 52, 48, 47, 49, 53]      
aqi = [110, 120, 130, 140, 135, 125, 115, 118, 122, 128] 

def calculate_average(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]

    return median

avg_temp = calculate_average(temperature)
median_temp = calculate_median(temperature)

avg_humidity = calculate_average(humidity)
median_humidity = calculate_median(humidity)

avg_aqi = calculate_average(aqi)
median_aqi = calculate_median(aqi)

print("📊 Weather & AQI Analysis for Gandhinagar (Last 10 Days)\n")

print("🌡 Temperature:")
print("Average:", round(avg_temp, 2), "°C")
print("Median :", median_temp, "°C\n")

print("💧 Humidity:")
print("Average:", round(avg_humidity, 2), "%")
print("Median :", median_humidity, "%\n")

print("🌫 AQI (Air Quality Index):")
print("Average:", round(avg_aqi, 2))
print("Median :", median_aqi)
