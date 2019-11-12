import time

# for i in range(1,11):
#     time.sleep(1)
#     loop_count = i
#     print_str = None
#     while loop_count > 0:
#         if loop_count == i:
#             print_str = '*'
#         else:
#             print_str += '*'
#         loop_count -= 1
#     print(print_str)

for i in range(1,11):
    time.sleep(1)
    print('*' * i)