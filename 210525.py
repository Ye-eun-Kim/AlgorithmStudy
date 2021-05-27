def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        short = min(phone_book[i], phone_book[i+1])
        long = max(phone_book[i], phone_book[i+1])
        if short in long[0:len(short)] :
            return False
    return True

phone_book = ["123","456","789"]
a = solution(phone_book)
