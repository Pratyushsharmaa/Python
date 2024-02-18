print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
count_t = lower_names.count("t")
count_r = lower_names.count("r")
count_u = lower_names.count("u")
count_e = lower_names.count("e")
total1 = count_t + count_r + count_u + count_e
count_l = lower_names.count("l")
count_o = lower_names.count("o")
count_v = lower_names.count("v")
count_E = lower_names.count("e")
total2 = count_l + count_o + count_v + count_E

final_score = int(str(total1) + str(total2))

if final_score<10 or final_score>90:
 print(f"Your score is {final_score}, you go together like coke and mentos.")

elif 40<=final_score<=50:
 print(f"Your score is {final_score}, you are alright together. ")

else:
 print(f"Your score is {final_score}.")