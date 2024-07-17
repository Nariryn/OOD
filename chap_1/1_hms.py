print ("*** Converting hh.mm.ss to seconds ***")

hh, mm, ss = map(int, input("Enter hh mm ss : ").split())

if mm > 59 or mm < 0:
    print(f"mm({mm}) is invalid!")
else:
    total_sec = (hh * 3600) + (mm * 60) + ss
    print (f"{hh:02}:{mm:02}:{ss:02} = {total_sec:,} seconds")