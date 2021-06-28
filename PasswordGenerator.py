import random
import array

Max_len =12

D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
L_C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
U_C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
S = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

C_L = D + L_C + U_C + S

rand_digit = random.choice(D)
rand_upper = random.choice(U_C)
rand_lower = random.choice(L_C)
rand_symbol = random.choice(S)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(Max_len - 4):
    temp_pass = temp_pass + random.choice(C_L)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x

print(password)