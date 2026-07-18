"""Saitama"""
pushup = int(input())
situp= int(input())
squat = int(input())
run = int(input())
push_day = int(input())
sit_day = int(input())
run_day = int(input())
squat_day = int(input())

d1 = (pushup + push_day - 1) // push_day
d2 = (situp + sit_day - 1) // sit_day
d3 = (squat + squat_day - 1) // squat_day
d4 = (run + run_day - 1) // run_day

print(max(d1, d2, d3, d4))
