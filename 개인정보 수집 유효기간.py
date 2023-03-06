from datetime import datetime
from dateutil.relativedelta import relativedelta
https://github.com/frost0807/coding-test-study.git
C:\Users\emily\PycharmProjects\CodingTest\codingtest_study

# TypeError: Object of type datetime is not JSON serializable
def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, "%Y.%m.%d")
    for i in range(len(privacies)):
        list_privacy = privacies[i].split()
        privacy_date = list_privacy[0]
        pd = datetime.strptime(privacy_date, "%Y.%m.%d")
        pv = list_privacy[1]
        pvm = 0

        for j in range(len(terms)):
            if pv in terms[j]:
                a = terms[j].split()
                pvm = int(a[1])

        # pvd = pvm*28
        pd = pd + relativedelta(months=pvm)
        if pd <= today:
            answer.append(i+1)

    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))