def enlogicate(strs):
    strs = strs.split()
    i = 0
    while i < len(strs):
        if str(strs[i]).lower() == "AND".lower() or str(strs[i]).lower() == "N".lower() or  str(strs[i]).lower() == "^":
            strs[i] = "*"
        if str(strs[i]).lower() == "OR".lower() or str(strs[i]).lower() == "U".lower() or  str(strs[i]).lower() == "V".lower():
            strs[i] = "+"
        if (str(strs[i]).lower() == "NOT".lower() or  str(strs[i]).lower() == "~") and strs[i+1] != " ":
            strs[i+1] = str(1) if int(strs[i+1]) == 0 else str(0)
            strs.pop(i)
            i-=1
        i+=1
    return 0 if eval(' '.join(strs)) == 0 else 1


print(enlogicate("1 or ( 1 and 0 )"))
