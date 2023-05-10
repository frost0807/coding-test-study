// https://school.programmers.co.kr/learn/courses/30/lessons/135807
// 단순 GCD 문제
const gcd = (a, b) => b == 0 ? a : gcd(b, a % b);
function solution(A, B) {
    const am = A.reduce((a, b) => gcd(a, b));
    const bm = B.reduce((a, b) => gcd(a, b));
    const mods = [B.every(x => x % am) ? am : 0, A.every(x => x % bm) ? bm : 0];
    return Math.max(...mods);
}