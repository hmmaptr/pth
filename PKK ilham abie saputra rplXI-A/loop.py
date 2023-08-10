# while
x = 1
while (x<6):
    print(x);
    x+=1;

#for
i = 1
for i in range (6):
    print(x);
    i+=1;

import re;
print("merubah huruf");

listkota = ['solo', 'surabaya', 'bekasi', 'jakarta'];

listhurufvokal = ['a', 'i', 'u', 'e', 'o'];

for kota in listkota:
    print('[' + kota + ']');
    for vokal in listhurufvokal:
        print('--->' + re.sub('[aiueo]', vokal, kota));