# aks to person that he say anything text real
#calulate how much time pass while him say that
#how many words he said?

# 2 word for 1 second

text = input("please, say any text please: ")

words_that_a_person_normal_say_within_1_second = 2
words_of_text = text.split()
time_pass_while_he_say = len(words_of_text) / words_that_a_person_normal_say_within_1_second

print(f"the time pass while he say this is {time_pass_while_he_say}s")



# if the time is more than 1 minute say him anything
if time_pass_while_he_say >= 60:
    print('hey guy stop, i do not aks you a biblia ')
else:
    print("that is very good")

#dalto talk a 30% faster
# how much time pass while he say that  

words_that_dalto_say_in_1_second = words_that_a_person_normal_say_within_1_second+ words_that_a_person_normal_say_within_1_second*100 //30 /10

print(words_that_dalto_say_in_1_second)

time_pass_dalto_said_the_text = len(words_of_text) * 100 // words_that_dalto_say_in_1_second /100

print(f"the time pass while dalto say this is {time_pass_dalto_said_the_text}s")
