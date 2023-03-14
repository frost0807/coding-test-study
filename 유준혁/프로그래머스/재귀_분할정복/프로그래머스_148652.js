// https://school.programmers.co.kr/learn/courses/30/lessons/148652?language=javascript#
/*
    생각보다 어려워서 고전함.
    재귀로 푸는 방식은 금방 생각했으나 세부 조건들을 세팅하는데 꽤 걸림
    중요 아이디어
    1. 5 ** n (n > 1) 일 때 가운데 부분은 항상 0이다. (체크하지 않아도 된다.)
    2. 5 ** (n - 1) 의 5개 부분으로 나누었을 때 (x1 ~ x2) 아래와 같이 구별할 수 있다.
        2-1. l이 포함되는 부분 (l ~ x2)
        2-2. 완전히 l < x < r 인 부분 (1의 개수가 4 ** (n - 1)인 부분)
        2-3. r이 포함되는 부분 (x1 ~ r)
    3. 2-2는 단순 계산으로 합하고 2-1, 2-3에 대해서만 재귀를 수행
*/
const count = (n, l, r) => {
    let pow = Math.pow(5, n - 1), cnt = 0;
    if (n === 1) {
        for(var i = 0, L = l % 5, R = r; i < 5; i++) {
            if (i !== 2 && L <= i && i < R) cnt++;
        }
    } else {
        for(let i = 0; i < 5; i++) {
            let f = pow * i, a = Math.max(f, l), b = Math.min(f + pow, r);
            if (i === 2 || b <= l || r <= a) continue;
            if (a % pow == 0 && b % pow == 0) cnt += Math.pow(4, n - 1);
            else cnt += count(n - 1, a % pow, b % pow == 0 ? pow : (b % pow));
        }
    }
    return cnt;
}
function solution(n, l, r) {
    return count(n, l - 1, r);
}