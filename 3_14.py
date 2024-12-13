a=float(input())
#print(int(a//30))
#print(int(a%30/30*60))
#print(int((a%30/30*60)%1*60))
dol_ch=a%30/30
past_sec=dol_ch*3600
ans=int(past_sec%60)