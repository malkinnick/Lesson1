def discounted(price, discount, max_discount=30, phone_name=''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower or not phone_name:
        return price
    else:
        return price - (price * discount / 100)


new_price = discounted (100000, 10, phone_name ='iPhone 12')
print(new_price)=100000

new_price = discounted (40000, 20, phone_name ='Samsung')
print(new_price)=32000

new_price = discounted (40000, 20, phone_name ='Xiaomi Mi11')
print(new_price)=5000