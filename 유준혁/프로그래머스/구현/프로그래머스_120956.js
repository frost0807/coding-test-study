const strings = [];
const dfs = (n, str, bit) => {
    if (n > 4) return;
    if (n) strings.push(str);
    for(let i = 0; i < 4; i++) {
        if (bit & (1 << i)) continue;
        dfs(n + 1, str + ['aya', 'ye', 'woo', 'ma'][i], bit | (1 << i));
    }
}
function solution(babbling) {
    dfs(0, '', 0);
    return babbling.filter(x => strings.includes(x)).length;
}
