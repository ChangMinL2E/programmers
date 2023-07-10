def solution(a, b, c, d):
    lst = [a,b,c,d]
    p,q,r = 0,0,0
    answer = 0
    maximum = 0
    setOfLst = []
    for element in lst:
        if lst.count(element) > maximum:
            maximum = lst.count(element)
    
    if maximum == 4:
        answer = a*1111
    elif maximum == 3:
        setOfLst = list(set(lst))
        for ele in setOfLst:
            print(lst.count(ele))
            if lst.count(ele) == 3:
                p = ele
            else:
                q = ele
        answer = (10*p+q)**2
        
    elif maximum == 2:
        setOfLst = list(set(lst))
        if len(setOfLst) == 2:
            for ele in setOfLst:
                if p==0:
                    p = ele
                else:
                    q = ele
            answer = (p+q)*abs(p-q)
        else:
            for ele in setOfLst:
                if lst.count(ele) == 1:
                    if p == 0:
                        p = ele
                    else:
                        q = ele
            answer = p*q
            
    else:
        answer = min(lst)
    
    
    
    
    return answer