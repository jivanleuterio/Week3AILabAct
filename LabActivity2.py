def check_fast_lane(minutes_left, items, teacher_pass):
    if minutes_left > 1 and minutes_left <=10 and items <= 3 and items >=1 or teacher_pass == True:
        return "Fast lane approved"
    elif minutes_left >= 0 and items >= 0:
        return "Use regular line"
    else:
        return "Error: Invalid Input"

students_in_fast_lane = 0
students_in_line = [
    {"name": "Marco", "minutes_left": 8, "items": 2, "teacher_pass": False},
    {"name": "Diane", "minutes_left": 15, "items": 1, "teacher_pass": False},
    {"name": "Kyle", "minutes_left": 5, "items": 6, "teacher_pass": False},
    {"name": "Ella", "minutes_left": 20, "items": 5, "teacher_pass": True},
]

for students in students_in_line:
    print("Student:", students["name"])
    print("Minutes Left:", students["minutes_left"])
    print("Items:", students["items"])
    print("Teacher Pass:", students["teacher_pass"])
    fast_lane_status = check_fast_lane(students["minutes_left"], students["items"], students["teacher_pass"])

    print("Status:", fast_lane_status)
    if fast_lane_status == "Fast lane approved":
        students_in_fast_lane += 1
    print()

print("Total students in fast lane:", students_in_fast_lane)
