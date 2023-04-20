# import pandas as pd

list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    # df1 = pd.DataFrame(list1)
    # df2 = pd.DataFrame(list2)
    # merged_df = pd.merge(df1, df2, on='id', how='outer')
    # merged_list = merged_df.to_dict(orient='records')

    # return merged_list

    student_ids = set()
    result = []
    for student in list_1:
        student_ids.add(student['id'])
    for student in list_2:
        student_ids.add(student['id'])

    for student_id in student_ids:
        merged_student = {}
        for student in list_1 + list_2:
            if student['id'] == student_id:
                merged_student.update(student)
        result.append(merged_student)

    return result


list_3 = merge_lists(list_1, list_2)
# print(list_3)
