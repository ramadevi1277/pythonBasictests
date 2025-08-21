list1= [{"emp":"john", "dest_no" : "QA Engineer"},{"emp":"Rama", "dest_no": "Software_eng"},{"emp":"devi", "dest_no": "engineer"}]

for each in range(len(list1)):
    print("emp is %s" %(list1[each]['emp']), end=" and ")
    print("dest_no is %s"  %(list1[each]['dest_no']))
    print(f"Employe is {list1[each]['emp']} and dest_no is {list1[each]['dest_no']}")


for each_dict in list1:
    print(f"employee is {each_dict['emp']} and designation is {each_dict['dest_no']}")