# 문자열로 된 식 실행하기 (eval)
expr1='2+3'
expr2='round(3.7)' #round(n) : n을 반올림 한 수
ret1=eval(expr1)
ret2=eval(expr2)
print('<%s>를 eval()로 실행한 결과: ' %expr1, end=''); print(ret1)
print('<%s>를 eval()로 실행한 결과: ' %expr2, end=''); print(ret2)

#이름없는 한줄짜리 함수 만들기 (lambda)
add=lambda x,y:x+y
ret=add(1,3)
print(ret)  #4가 출력

funcs=[lambda x:x+'.pptx', lambda x:x+'docx']
ret1=funcs[0]('intro')
ret2=funcs[1]('Report')
print(ret1) #intro.pptx가 출력
print(ret2) #Report.pptx가 출력

names={'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
ret3=sorted(names.items(), key=lambda x:x[0])
print(ret3)