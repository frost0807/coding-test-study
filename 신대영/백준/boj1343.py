# 첫번째 풀이 : 콤마로 구분해서 리스트업후 문자열길이로 검증후 문자열 변경하는 방식으로 해결
a = input()
a_list = a.split('.')

is_success = True

for i, b in enumerate(a_list):
    n = len(b)
    if (n % 4) % 2 == 0:
        a_list[i] = 'AAAA' * (n // 4) + 'BB' * ((n % 4) // 2)
    else:
        is_success = False
        break
        
print(".".join(a_list) if is_success else '-1')

# 두번째 풀이 : 차례대로 문자열 변환후 변경되지 않은 "X"를 찾아서 해결
a = input()
b = a.replace("XXXX", "AAAA").replace("XX","BB")
print("-1" if "X" in b else b)