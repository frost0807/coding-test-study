let min = 1 << 30, n, m, b, t;
const xflip = (arr) => arr.map(x => x ^ 1);
const yflip = (arr, i) => arr.map(x => x.map((y, idx) => idx === i ? y ^ 1 : y));
const isSame = (b, t) => {
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < m; j++) {
            if (b[i][j] !== t[i][j]) return false;
        }
    }
    return true;
}
const dfs = (idx, bit) => {
    if (idx === n) {
        let cnt = 0, flip = [ ...b ];
        for(let i = 0; i < n; i++) {
            if (bit & (1 << i)) {
                flip[i] = xflip(flip[i]);
                cnt++;
            }
        }
        for(let j = 0; j < m; j++) {
            if (!flip.every((x, i) => x[j] === t[i][j])) {
                flip = yflip(flip, j);
                cnt++;
            }
        }
        if (isSame(flip, t)) min = Math.min(min, cnt);
    } else {
        dfs(idx + 1, bit);
        dfs(idx + 1, bit | (1 << idx));
    }
}
function solution(beginning, target) {
    [b, t, n, m] = [beginning, target, beginning.length, beginning[0].length];
    dfs(0, 0);
    return min === 1 << 30 ? -1 : min;
}