from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('ping.csv')

latency_values = data['latency']

plt.plot(latency_values, label='Latency to 8.8.8.8')

plt.xlabel('Time')
plt.ylabel('Latency (ms)')
plt.title('Latency through time')

plt.legend()

plt.show()
