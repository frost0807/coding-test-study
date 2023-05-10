// https://school.programmers.co.kr/learn/courses/30/lessons/131130?language=javascript
// 사이클 판별 단순 구현 문제
function solution(cards, groups = []) {
    cards = cards.map(x => x - 1);
    while(!cards.every(x => x === -1)) {
        let idx = cards.findIndex(x => x != -1), group = [];
        while(cards[idx] != -1) {
            let val = cards[idx];
            cards[idx] = -1;
            group.push(val);
            idx = val;
        }
        groups.push(group.length);
    }
    groups = groups.sort((a, b) => b - a);
    return groups.length < 2 ? 0 : (groups[0] * groups[1]);
}