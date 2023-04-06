// https://school.programmers.co.kr/learn/courses/30/lessons/150365?language=javascript
const answer = [], wh = [[1, 0, 0, -1], [0, -1, 1, 0], ['d', 'l', 'r', 'u']];
let N, M, X, Y, R, C, K;
const dfs = (x, y, k, path) => {
    const plus = k - (Math.abs(R - x) + Math.abs(C - y));
    if (answer.length || plus < 0) return;
    if (k) {
        for(let i = 0; i < 4; i++) {
            const n = x + wh[0][i], m = y + wh[1][i];
            if (n && m && n <= N && m <= M) dfs(n, m, k - 1, [ ...path, [i]]);
        }
    } else {
        if (x === R && y === C) answer.push(path);
    }
}
function solution(n, m, x, y, r, c, k) {
    [N, M, X, Y, R, C, K] = [n, m, x, y, r, c, k];
    let tox = r - x, toy = c - y, plus = k - (Math.abs(r - x) + Math.abs(c - y));
    if (plus < 0 || plus % 2 > 0) return 'impossible';
    dfs(x, y, k, []);
    return answer[0].map(x => wh[2][x]).join('');
}