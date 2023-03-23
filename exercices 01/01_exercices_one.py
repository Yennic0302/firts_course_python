normal_courses_times = {
    "min": 2.5,
    "pro": 4,
    "max": 7
}
time_without_edit = 5
time_with_edit = 4

dalto_time_without_edit = 3.5 
dalto_course = 1.5

#a) deference in percentage beetween dalto course and other courses
# the faster than other courses 
# the slower than other courses 
# the promedio other courses 

#b) porcentage of material bad reduce in
# the promedio of the courses
# the promedio of the current course

#b) watch 10 hours of this course is equal to other courses? and reverse?

deference_between_min_and_dalto=100 - dalto_course / normal_courses_times["min"] * 100
print(deference_between_min_and_dalto)

deferece_beetween_max_and_dalto = 100 - dalto_course *1000 // normal_courses_times["max"] / 10
print(deferece_beetween_max_and_dalto)

deference_between_pro_and_dalto = 100 -dalto_course / normal_courses_times["pro"] *100
print(deference_between_pro_and_dalto)

promedio_between_mateial_edited_other_course = 100 - time_with_edit / time_without_edit *100
print(promedio_between_mateial_edited_other_course)

promedio_between_mateial_edited_current_course = 100 - dalto_course *1000 // dalto_time_without_edit /10
print(promedio_between_mateial_edited_current_course)

hour_of_this_course_is_equal= (normal_courses_times["pro"]* 100 //dalto_course / 10 )
print(hour_of_this_course_is_equal)

hour_of_other_course_is_equal= (dalto_course* 100 //normal_courses_times["pro"] / 10 )
print(hour_of_other_course_is_equal)