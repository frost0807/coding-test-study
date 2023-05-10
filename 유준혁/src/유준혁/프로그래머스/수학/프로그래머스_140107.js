// https://school.programmers.co.kr/learn/courses/30/lessons/140107
function solution(k, d, cnt = 0) {
    for(let i = 0; i <= d; i += k) {
        let j = Math.sqrt(d * d - i * i);
        cnt += Math.floor(j / k) + 1;
    }
    return cnt;
}