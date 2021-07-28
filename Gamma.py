def solution(S):
    n = round(len(S))
    counter = 0
    for i in range(0,n):
        for ii in range(0,i):
            if S[ii:i+1] == S[ii:i+1][::-1]:
                counter = counter+1
                if counter > 100000000:
                    return -1
    return counter