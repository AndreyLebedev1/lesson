import requests
import time
r = requests.get('http://127.0.0.1:9999/cities')

#num_of_iter = 1000
#for i in range(num_of_iter):
print("Input n:")
n = input()
t0 = time.time()

for i in range(1,int(n)):
    f = requests.get(f'http://127.0.0.1:9999/fib/{i}')
    print(f.text)
t1 = time.time()
print(f"timestep:{t1-t0}")
#print(f.url)
#print(f.text)
#print(f.json())
