import random

candidates = ['가위', '바위', '보']
p1scissor, p1rock, p1paper = 0, 0, 0
p2scissor, p2rock, p2paper = 0, 0, 0

p1win, p1lose, p2win, p2lose, tie = 0, 0, 0, 0, 0

wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}

repeat = int(input('가위바위보를 몇 번 할까요?: '))

for i in range(repeat):
    p1select = random.choice(candidates)
    if p1select == '가위':
        p1scissor += 1
    elif p1select == '바위':
        p1rock += 1
    else:
        p1paper += 1

    p2select = random.choice(candidates)
    if p2select == '가위':
        p2scissor += 1
    elif p2select == '바위':
        p2rock += 1
    else:
        p2paper += 1

    print('{}번째 승부:'.format(i+1))

    '''
    if p1select == p2select:
        tie += 1
        print('당신과 상대 모두 {}를 내서 비김\n'.format(p1select))
    elif p1select == '가위' and p2select == '바위':
        p1lose += 1
        p2win += 1
        print('당신은 {}로 패 / 상대는 {}로 승\n'.format(p1select, p2select))
    elif p1select == '가위' and p2select == '보':
        p1win += 1
        p2lose += 1
        print('당신은 {}로 승 / 상대는 {}로 패\n'.format(p1select, p2select))
    elif p1select == '바위' and p2select == '가위':
        p1win += 1
        p2lose += 1
        print('당신은 {}로 승 / 상대는 {}로 패\n'.format(p1select, p2select))
    elif p1select == '바위' and p2select == '보':
        p1lose += 1
        p2win += 1
        print('당신은 {}로 패 / 상대는 {}로 승\n'.format(p1select, p2select))
    elif p1select == '보' and p2select == '가위':
        p1lose += 1
        p2win += 1
        print('당신은 {}로 패 / 상대는 {}로 승\n'.format(p1select, p2select))
    elif p1select == '보' and p2select == '바위':
        p1win += 1
        p2lose += 1
        print('당신은 {}로 승 / 상대는 {}로 패\n'.format(p1select, p2select))
    '''

    if p1select == p2select:
        tie += 1
        print('당신과 상대 모두 {}를 내서 비김\n'.format(p1select))
    elif wintable[p1select] == p2select:
        p1win += 1
        p2lose += 1
        print('당신은 {}로 승 / 상대는 {}로 패\n'.format(p1select, p2select))
    else:
        p1lose += 1
        p2win += 1
        print('당신은 {}로 패 / 상대는 {}로 승\n'.format(p1select, p2select))


print('총 {}회 가위바위보 결과'.format(repeat))
print('\n')
print('당신은 가위 {}번, 바위 {}번, 보 {}번을 냈습니다.'.format(p1scissor, p1rock, p1paper))
print('그 결과 {}승 {}무 {}패를 했습니다'.format(p1win, tie, p1lose))
print('\n')
print('상대는 가위 {}번, 바위 {}번, 보 {}번을 냈습니다.'.format(p2scissor, p2rock, p2paper))
print('그 결과 {}승 {}무 {}패를 했습니다'.format(p2win, tie, p2lose))

