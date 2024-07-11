import random

n = int(input('Enter the desired length of password'))
AC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
AS = "abcdefghijklmnopqrstuvwxyz"
AN = "1234567890"
ASY = "!@#$%^&*?,."
ALL = AC+AS+AN+ASY
password = ''.join(random.choice(ALL) for i in range(n))
print(password)