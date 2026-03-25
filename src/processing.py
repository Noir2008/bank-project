def filter_by_state(list_transitions, state="EXECUTED"):
    new_list_transitions = []

    for transition in list_transitions:
        if transition["state"] == "":
            transition["state"] = "EXECUTED"

        if transition["state"] == state:
            new_list_transitions.append(transition)

    return new_list_transitions


def sort_by_date(list_transitions, reverse=False):
    # new_list_transitions = []
    # new_list_transitions.extend(list_transitions)

    # new_list_transitions.sort(key=lambda x: x["date"], reverse=reverse)

    new_list_transitions = sorted(list_transitions,
                                  key=lambda x: x["date"], reverse=reverse
                                  )

    return new_list_transitions


transitions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:30:00.000",
        "amount": 5000
    },
    {
        "id": 2,
        "state": "CANCELED",
        "date": "2024-01-10T14:20:00.000",
        "amount": 1000
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2024-01-20T09:15:00.000",
        "amount": 2500
    },
    {
        "id": 4,
        "state": "CANCELED",
        "date": "2026-01-20T09:12:25.120",
        "amount": 2500
    },
    {
        "id": 5,
        "state": "",
        "date": "2025-01-10T14:27:15.800",
        "amount": 1000
    }
]

# возвращает транзакции 1, 3 и 4
print(filter_by_state(transitions))
# возвращает транзакции 2 и 5
print(filter_by_state(transitions, "CANCELED"))
print()
# порядок - сначала старые (2, 1, 3, 5, 4)
print(sort_by_date(transitions))
# порядок - сначала новые (4, 5, 3, 1, 2)
print(sort_by_date(transitions, True))