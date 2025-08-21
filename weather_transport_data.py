import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
def load_weather_data():
    df = pd.read_csv("weather_monthly.csv", skiprows=1)  # adjust skiprows if needed
    # Ensure 'Date' column is datetime for merging/plotting
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    return df

def load_transport_data():
    df = pd.read_csv("transport_performance.csv")  # trains, buses, ferries
    # Ensure 'Date' column is datetime for merging/plotting
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    return df

# Example analysis
def summary_statistics():
    weather = load_weather_data()
    transport = load_transport_data()

    print("\n--- Weather Summary ---")
    print(weather.describe(include='all'))

    print("\n--- Transport Summary ---")
    print(transport.describe(include='all'))

def plot_rainfall_vs_trains():
    weather = load_weather_data()
    transport = load_transport_data()

    # Merge both datasets on Date (ensure 'Date' is present and formatted)
    if 'Date' not in weather.columns or 'Date' not in transport.columns:
        print("Error: 'Date' column missing in one of the datasets.")
        return

    merged = pd.merge(weather, transport, on="Date")

    # Check required columns exist
    if "Rainfall (mm)" not in merged.columns or "Train On-Time (%)" not in merged.columns:
        print("Error: Required columns missing for plotting.")
        return

    plt.figure(figsize=(8, 6))
    plt.scatter(merged["Rainfall (mm)"], merged["Train On-Time (%)"])
    plt.xlabel("Rainfall (mm)")
    plt.ylabel("Train On-Time (%)")
    plt.title("Rainfall vs Train Punctuality")
    plt.tight_layout()
    plt.savefig("rainfall_vs_trains.png")
    plt.show()

def plot_temp_trends():
    weather = load_weather_data()

    # Check required columns exist
    if "Date" not in weather.columns or "Max Temp (°C)" not in weather.columns or "Min Temp (°C)" not in weather.columns:
        print("Error: Required columns missing for plotting.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(weather["Date"], weather["Max Temp (°C)"], label="Max Temp")
    plt.plot(weather["Date"], weather["Min Temp (°C)"], label="Min Temp")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trends Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig("temperature_trends.png")
    plt.show()

def view_full_dataset():
    weather = load_weather_data()
    transport = load_transport_data()
    print("\n--- Weather Data ---")
    print(weather.head(10))
    print("\n--- Transport Data ---")
    print(transport.head(10))
