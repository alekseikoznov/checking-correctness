def find_json_diff(old, new, diff_list, path="", result=None):
    if result is None:
        result = {}

    for key in old:
        current_path = f"{path}.{key}" if path else key
        if key in new:
            if isinstance(old[key], dict) and isinstance(new[key], dict):
                find_json_diff(
                    old[key], new[key], diff_list, current_path, result
                )
            elif old[key] != new[key]:
                if any(part in current_path for part in diff_list):
                    nested_keys = current_path.split(".")[1:]
                    nested_result = result
                    for nested_key in nested_keys[:-1]:
                        nested_result = nested_result.setdefault(
                            nested_key, {}
                        )
                    nested_result[nested_keys[-1]] = new[key]

    return result


def main():
    json_old = {
        "company_id": 111111,
        "resource": "record",
        "resource_id": 406155061,
        "status": "create",
        "data": {
            "id": 11111111,
            "company_id": 111111,
            "services": [
                {
                    "id": 9035445,
                    "title": "Стрижка",
                    "cost": 1500,
                    "cost_per_unit": 1500,
                    "first_cost": 1500,
                    "amount": 1,
                }
            ],
            "goods_transactions": [],
            "staff": {"id": 1819441, "name": "Мастер"},
            "client": {
                "id": 130345867,
                "name": "Клиент",
                "phone": "79111111111",
                "success_visits_count": 2,
                "fail_visits_count": 0,
            },
            "clients_count": 1,
            "datetime": "2022-01-25T11:00:00+03:00",
            "create_date": "2022-01-22T00:54:00+03:00",
            "online": False,
            "attendance": 0,
            "confirmed": 1,
            "seance_length": 3600,
            "length": 3600,
            "master_request": 1,
            "visit_id": 346427049,
            "created_user_id": 10573443,
            "deleted": False,
            "paid_full": 0,
            "last_change_date": "2022-01-22T00:54:00+03:00",
            "record_labels": "",
            "date": "2022-01-22 10:00:00",
        },
    }
    json_new = {
        "company_id": 111111,
        "resource": "record",
        "resource_id": 406155061,
        "status": "create",
        "data": {
            "id": 11111111,
            "company_id": 111111,
            "services": [
                {
                    "id": 22222225,
                    "title": "Стрижка",
                    "cost": 1500,
                    "cost_per_unit": 1500,
                    "first_cost": 1500,
                    "amount": 1,
                }
            ],
            "goods_transactions": [],
            "staff": {"id": 1819441, "name": "Мастер"},
            "client": {
                "id": 130345867,
                "name": "Клиент",
                "phone": "79111111111",
                "success_visits_count": 2,
                "fail_visits_count": 0,
            },
            "clients_count": 1,
            "datetime": "2022-01-25T13:00:00+03:00",
            "create_date": "2022-01-22T00:54:00+03:00",
            "online": False,
            "attendance": 2,
            "confirmed": 1,
            "seance_length": 3600,
            "length": 3600,
            "master_request": 1,
            "visit_id": 346427049,
            "created_user_id": 10573443,
            "deleted": False,
            "paid_full": 1,
            "last_change_date": "2022-01-22T00:54:00+03:00",
            "record_labels": "",
            "date": "2022-01-22 10:00:00",
        },
    }
    diff_list = ["services", "staff", "datetime"]

    result = find_json_diff(json_old, json_new, diff_list)
    print(result)


if __name__ == "__main__":
    main()
