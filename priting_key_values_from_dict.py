
def print_employee_details(data):
    for item in data:
        if isinstance(item, dict):
            print(f"employee is {item['emp']} and designation is {item['dest_no']}")
        elif isinstance(item, list):
            print_employee_details(item)

list1 = [
    {"emp": "john", "dest_no": "QA Engineer"},
    [
        {"emp": "Rama", "dest_no": "Software_eng"},
        {"emp": "devi", "dest_no": "engineer"}
    ]
]

print_employee_details(list1)