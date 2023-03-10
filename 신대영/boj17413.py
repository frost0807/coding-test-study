words = input().rstrip()

# 태그 '<' 시작하고 '>' 완료된 문자열은 그대로 출력
# 나머지 문자열은 뒤집어서 출력

isTag = False

result = ""
tmp_word = ""

for word in words:
    # 태그 여부 확인
    # 그래도 출력
    if isTag:
        if word == '>':
            isTag = False
        result += word
    else:
        if word == '<':
            isTag = True
            result += tmp_word[::-1] + word
            tmp_word = ''
        elif word == ' ':
            result += tmp_word[::-1] + word
            tmp_word = ''
        else:
            tmp_word += word
            
result += tmp_word[::-1] if tmp_word else ''

print(result)