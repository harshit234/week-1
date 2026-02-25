
temperature = [32, 34, 33, 35, 36, 34, 33, 32, 31, 35]   
humidity = [45, 50, 55, 60, 58, 52, 48, 47, 49, 53]      

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

print("📊 Weather Analysis for Gandhinagar (Last 10 Days)\n")

print("🌡 Temperature:")
print("Average Temperature:", round(avg_temp, 2), "°C")
print("Median Temperature:", median_temp, "°C\n")

print("💧 Humidity:")
print("Average Humidity:", round(avg_humidity, 2), "%")
print("Median Humidity:", median_humidity, "%")
