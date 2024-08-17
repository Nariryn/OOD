print('*** Converting hh.mm.ss to seconds ***')
h,m,s=input('Enter hh mm ss : ').split()
result = int(h)*60*60 + int(m)*60 + int(s)
if int(m)<0 or int(m)>=60:
    print(f"mm({m}) is invalid!") 
elif int(s)<0 or int(s)>=60:
    print(f"ss({s}) is invalid!")   
else:
    print(f"{h:>02}:{m:>02}:{s:>02} = {result:,} seconds")