def solution(price, money, count):
    spend = sum([price * i for i in range(1,count+1)])
    return spend - money if spend - money > 0 else 0