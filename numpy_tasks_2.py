import numpy as np

print("Завдання 1")
image_matrix = np.array([
    [100, 150, 200, 250],
    [50, 120, 180, 220],
    [30, 90, 140, 190],
    [10, 50, 100, 150]
])
dark = np.clip(image_matrix - 20, 0, 255)
print("Затемнене зображення:")
print(dark)
print("Середня інтенсивність:", dark.mean())

print("\nЗавдання 2")
coordinates = np.array([[1.5, 2.0], [5.0, 8.1], [3.2, 1.1], [8.9, 4.3], [2.1, 2.8]])
x, y = coordinates.T
print("X:", x)
print("Y:", y)
print("Максимум X:", x.max())
print("Мінімум Y:", y.min())
mask = (x + y) > 6.0
print("Координати з X + Y > 6.0:")
print(coordinates[mask])

print("\nЗавдання 3")
stock_prices = np.array([100.0, 102.5, 101.0, 105.0, 104.2, 108.0, 110.5])
today = stock_prices[1:]
yesterday = stock_prices[:-1]
returns = (today - yesterday) / yesterday
print("Ціни сьогодні:", today)
print("Ціни вчора:", yesterday)
print("Дохідність:", returns)
best = np.argmax(returns)
print("День з найвищою дохідністю:", best + 1)
print("Значення дохідності:", returns[best])

print("\nЗавдання 4")
sensor_data = np.array([23.4, 24.1, -999, 25.0, 26.2, -999, 24.8])
bad = sensor_data == -999
print("Маска пропущених значень:", bad)
mean_value = sensor_data[~bad].mean()
print("Середнє без пропусків:", mean_value)
fixed = np.where(bad, mean_value, sensor_data)
print("Масив після заміни:", fixed)

print("\nЗавдання 5")
inventory = np.array([12, 45, 23, 67, 89, 34, 50])
target = 40
diff = np.abs(inventory - target)
print("Абсолютні різниці:", diff)
idx = np.argmin(diff)
print("Індекс найближчого елемента:", idx)
print("Найближче значення:", inventory[idx])
