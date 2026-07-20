def check_fast_lane(minutes_left, items, teacher_pass):
    if teacher_pass == True or minutes_left > 1 and minutes_left <=10 and items <= 3 and items >=1:
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

# Explain in 5-9 sentences why rule-based systems need explicit "override" conditions like this, and what might go wrong if Aliah forgets to code the override check before the time/item check instead of after.
# What if two rules conflict — EXAMPLE a student has a teacher's pass but the cafeteria is currently closed for cleaning?
# How would Aliah's program need to change to handle a rule that overrides even the teacher's pass
# Answer: uhm rule based systems needs explicit override because some rules
# are more important than the other normal ones. Because override tells program to avoid or ignore the usual rules when a special conditions applies
# if she forgets to code the override check before time or item checks the system will make a wrong decision
# for example a student with a teacher pass can be denied because the system check the time, items first so if that first work and its denied without reading if he/she has teacher pass, it will give wrong output.
# if two rules conflict, system needs to follow the rules with the highest priority.
# example if the students has a teacher pass, they should not be allowed to enter if the cafeteria is closed for cleaning. because cleaning the cafeteria is more important.abs
# the program would need to check the rule with highest priority first before, checking the teachers pass for example is should check first
# if the cafeteria is closed for cleaning, if it is closed, the entry will be deny immediatly, even with the teachers pass
# flow: check cafeteria status >>>> if open >>>> priority teachers pass >>>> and students time/items check.