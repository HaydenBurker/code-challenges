# Create a class that has a variable count which counts the total number of instances created

class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1

print(InstanceCounter.count) # 0

InstanceCounter()
print(InstanceCounter.count) # 1

InstanceCounter()
InstanceCounter()
print(InstanceCounter.count) # 3

for i in range(10):
    InstanceCounter()
print(InstanceCounter.count) # 13