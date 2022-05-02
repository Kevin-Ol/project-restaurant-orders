import csv


def read_csv(filename):
    orders = {}
    menu = set()
    days_open = set()

    with open(filename) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for costumer, order, day in reader:
            if costumer not in orders:
                orders[costumer] = [(order, day)]
            else:
                orders[costumer].append((order, day))

            menu.add(order)
            days_open.add(day)

    return orders, menu, days_open


def most_ordered(orders):
    frequency = {}
    product = orders[0][0]

    for order, _day in orders:
        if order not in frequency:
            frequency[order] = 1
        else:
            frequency[order] += 1

        if frequency[order] > frequency[product]:
            product = order

    return product


def product_order_quantity(orders, product):
    counter = 0

    for order, _day in orders:
        if order == product:
            counter += 1

    return counter


def product_order_costumer(orders):
    return set([order[0] for order in orders])


def day_order_costumer(orders):
    return set([order[1] for order in orders])


def analyze_log(path_to_file):
    file_extension = path_to_file.split(".")[-1]

    if file_extension != "csv":
        raise FileNotFoundError(f"Extensão inválida {path_to_file}")

    try:
        orders, menu, days_open = read_csv(path_to_file)

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente {path_to_file}")

    most_ordered_maria = most_ordered(orders["maria"])
    hamburguer_ordered_arnaldo = product_order_quantity(
        orders["arnaldo"], "hamburguer"
    )
    product_not_ordered_joao = menu.difference(
        product_order_costumer(orders["joao"])
    )
    day_not_ordered_joao = days_open.difference(
        day_order_costumer(orders["joao"])
    )

    with open("data/mkt_campaign.txt", "w") as file2:
        rows = [
            most_ordered_maria,
            hamburguer_ordered_arnaldo,
            product_not_ordered_joao,
            day_not_ordered_joao,
        ]

        file2.writelines([f"{str(item)}\n" for item in rows])
