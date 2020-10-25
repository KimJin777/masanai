def makeURL(**kargs):
    myUrl = "http://www.naver.com/index.php?"

    i = 0

    for k, v in kargs.items():
        myUrl += k + '=' + v + "&"
        i = i+1
        print(i,"  ", kargs.items())
        print(i,"  ", myUrl)

    myUrl = myUrl.rstrip('&')
    print(myUrl)


makeURL(user='psychoria', index='5', page='10')