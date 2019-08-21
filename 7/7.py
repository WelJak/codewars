def find_outlier(integers):
    even=0
    odds=0
    for integer in integers:
        result=integer%2
        if result ==1:
            odds+=1
            output1=integer
        else:
            even+=1
            output2=integer
    if odds==1:
        return output1
    elif even==1:
        return output2
