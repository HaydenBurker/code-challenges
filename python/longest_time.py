# Create a function that takes in three numbers (hours, minutes, seconds) and returns the value that's the longest duration

def longest_time(h, m, s):
    second_times = [h * 3600, m * 60, s]
    longest_time = max(second_times)
    return h if second_times[0] == longest_time else m if second_times[1] == longest_time else s

print(longest_time(1, 58, 3599)) # 1
print(longest_time(2, 49, 1234)) # 49
print(longest_time(10, 100, 36001)) # 36001