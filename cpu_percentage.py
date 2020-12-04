import psutil

for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f'Core {i + 1}: {percentage}%')
print(f'Total CPU Usage: {psutil.cpu_percent()}%')
