// https://school.programmers.co.kr/learn/courses/30/lessons/178871
function solution(players, callings) {
    const dict = {};
    for(const i in players) dict[players[i]] = i;
    for(const call of callings) {
        const idx = dict[call];
        const temp = players[idx - 1];
        players[idx - 1] = call;
        players[idx] = temp;
        dict[call] = idx - 1;
        dict[temp] = idx;
    }
    return Object.entries(dict).sort((a, b) => a[1] - b[1]).map(x => x[0]);
}