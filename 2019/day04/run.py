def main():
    start = 124075
    stop = 580769
    count = 0
    for i in range(start, stop):
        if(meetCriteria(i)):
            count += 1
    print(meetCriteria(112233))
    print(meetCriteria(123444))
    print(meetCriteria(111122))
    print(count)

def meetCriteria(num):
    s = str(num)
    #increasing digits
    lastDigit = 0
    for c in s:
        digit = int(c)
        if(digit < lastDigit):
            return False
        lastDigit = digit

    #doubles
    lastDigit = None
    runLength = 1
    for c in s:
        if c == lastDigit:
            runLength += 1
        else:
            if runLength == 2:
                return True
            runLength = 1
        lastDigit = c

    if runLength == 2:
        return True
    return False

if __name__ == "__main__":
	main()