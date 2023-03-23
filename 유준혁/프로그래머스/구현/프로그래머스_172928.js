// https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=javascript
function solution(park, routes) {
    const n = park.length, m = park[0].length;
    const map = park.map(x => [...x]), dir = { 'E': [0, 1], 'S': [1, 0], 'W': [0, -1], 'N': [-1, 0]};
    var i = map.findIndex(x => x.includes('S')), j = map[i].findIndex(x => x === 'S');
    const move = (route) => {
        let [r, s] = route.split(' '), x = i, y = j;
        for(let k = 0; k < Number(s); k++) {
            x += dir[r][0];
            y += dir[r][1];
            if (x < 0 || y < 0 || x >= n || y >= m || map[x][y] === 'X') return [i, j];
        }
        return [x, y];
    }
    for(let route of routes) var [i, j] = move(route);
    return [i, j];
}