from treasures import treasures

def jumping(arr):
    minmem = -1
    maxmem = len(arr)
    sel = len(arr)//2 # une dist normoale de chiffre, plus de diversité de chiffres
    count = 1
    unvalid_idx = []
    while arr[sel] != "T":
        unvalid_idx.append(sel)
        info = arr[sel]
        if info >= 0 and info > minmem: minmem = info
        elif info < 0 and abs(info) < maxmem: maxmem = abs(info)
        sel = minmem + 1
        minmem += 1  
        count += 1 
    return(count)
