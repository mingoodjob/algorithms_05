"""
달팽이 올라감 낮에는 A미터 올라가고 밤에는 B미터 떨어짐
정상에 올라가면 미끄러지지 않음
A , B , V 공백으로 주어짐.
"""
A = 5
B = 1
V = 6
cnt = 0
high = 0

while True:
    high += A #2 #3 #4 #5   
    cnt += 1 #1 #2 #3
    if V <= high:
        break
    high -= B #1 #2 #3
    
    
print(cnt)
