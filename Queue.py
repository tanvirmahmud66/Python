from collections import deque

bank = deque(["X","Y","Z"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
if not bank:
    print("No one Left")
