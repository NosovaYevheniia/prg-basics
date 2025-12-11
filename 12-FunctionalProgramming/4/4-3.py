grade_list = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

result = list(filter(lambda grade: grade != 2.0, grade_list))
aver_grade = sum(result) / len(result)

print(f"Arithmetic mean for grades <> 2.0 is {aver_grade}")