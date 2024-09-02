def solution(order):
    am = 4500
    cafe = 5000
    price = 0
    for i in order:
        if 'am' in i:
            price += am
        elif 'cafe' in i:
            price += cafe
        else:
            price += am  
    return price