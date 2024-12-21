###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input("how many tasks ok: "))


if ((total_tasks / 2) < tasks_ok):
    print("Congratulations! You passed the test")
else:
    print("You've failed")
