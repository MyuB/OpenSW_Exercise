def alphaCnt(s):
        answer = 0
        for i in s:
                if i >= 'A' and i <= 'Z':
                        answer += 1
        return answer


cell = ['A51E', '12KB', 'KDD7',
        '1Z92', 'P703', 'GP2Y',
        'PPD4', 'PM7', '03Q', 'A3']
print(cell)
cell = sorted(cell, key=lambda x: (len(x), alphaCnt(x), x))
print(cell)

'''
람다 함수 연습하기
def alphaCnt(s) :
    answer = 0
    for i in s :
        if i >= "A" and i <= "Z" :
            answer += 1
    return answer


modelName = ["A51E", "12KB", "KDD7", "1Z92", "P703", "GP2Y", "PPD4", "PM7", "03Q", "A3"]
print(modelName)

modelName = sorted(modelName, key = lambda x : (len(x), alphaCnt(x), x))
print(modelName)
'''

