# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

#


prices = [13.52, 21.96, 13.05,  9.85, 67.74, 84.85, 15.61, 61.03, 91.30, 87.74, 58.91, 36.77, 74.96, 62.75, 25.44, 38.64,  5.55, 39.45, 71.39, 52.11]
for price in prices:
    rub = int(price)
    kk = (price-rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

prices = [13.52, 21.96, 13.05,  9.85, 67.74, 84.85, 15.61, 61.03, 91.30, 87.74, 58.91, 36.77, 74.96, 62.75, 25.44, 38.64,  5.55, 39.45, 71.39, 52.11]
print(id(prices))
prices.sort()
print(id(prices))
for price in prices:
    rub = int(price)
    kk = (price - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=',')


prices = [13.52, 21.96, 13.05,  9.85, 67.74, 84.85, 15.61, 61.03, 91.30, 87.74, 58.91, 36.77, 74.96, 62.75, 25.44, 38.64,  5.55, 39.45, 71.39, 52.11]
for price in sorted(prices) [::-1] [:5]:
    rub = int(price)
    kk = (price - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=',')


print([f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп' for price in sorted(prices)[::-1][5]])







