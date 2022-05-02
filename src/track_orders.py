class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self._orders_by_customer = {}
        self._orders_by_day = {}
        self._menu = set()
        self._days_open = set()

    def __len__(self):
        length = 0
        for value in self._orders_by_customer.values():
            length += len(value)

        return length

    def add_new_order(self, customer, order, day):
        if customer not in self._orders_by_customer:
            self._orders_by_customer[customer] = [(order, day)]
        else:
            self._orders_by_customer[customer].append((order, day))

        if day not in self._orders_by_day:
            self._orders_by_day[day] = 1
        else:
            self._orders_by_day[day] += 1

        self._menu.add(order)
        self._days_open.add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        orders = self._orders_by_customer[customer]
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

    def get_never_ordered_per_customer(self, customer):
        never_ordered = set(
            [order[0] for order in self._orders_by_customer[customer]]
        )

        return self._menu.difference(never_ordered)

    def get_days_never_visited_per_customer(self, customer):
        never_visited = set(
            [order[1] for order in self._orders_by_customer[customer]]
        )

        return self._days_open.difference(never_visited)

    def get_busiest_day(self):
        return max(self._orders_by_day, key=self._orders_by_day.get)

    def get_least_busy_day(self):
        return min(self._orders_by_day, key=self._orders_by_day.get)
