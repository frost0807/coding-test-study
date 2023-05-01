function solution(expression, max = 0) {
    const priority = [ '+-*', '+*-', '-+*', '-*+', '*-+', '*+-']; // 우선순위 6가지
    const tokens = expression.match(/([0-9]+|[\+\-\*])/g); // 수식 토큰화
    for(const p of priority) { // 각 우선순위에 대하여 절댓값 확인
        let sub = [ ...tokens ];
        for(const oper of [ ...p ]) { // '+-*' 인 경우 +, -, * 순서대로 연산
            let idx = -1;
            while((idx = sub.indexOf(oper)) > 0) { // 연산자가 있다면 1 <= idx <= sub.length - 1
                // 100-200*300-500+20 에서 *를 먼저 하는 경우라면
                // ['100', '-'], ['200', '*', '300'], ['-', '500', '+', '20'] 이렇게 3 구간으로 나눈 뒤
                // 가운데 구간만 계산하여 다시 합쳐줌
                sub = [
                    ...sub.slice(0, idx - 1),
                    eval(sub.slice(idx - 1, idx + 2).join('')),
                    // eval = 문자열로 된 코드를 실행하여 리턴
                    // eval('1 + 2') = 3
                    // eval('[2,4,5][1]') = 4
                    ...sub.slice(idx + 2),
                ];
            }
        }
        max = Math.max(max, Math.abs(Number(sub[0]))); //max 값 갱신
    }
    return max;
}