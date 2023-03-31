// https://school.programmers.co.kr/learn/courses/30/lessons/176963?language=javascript
function solution(name, yearning, photo) {
    const dict = {};
    for(let i in name) dict[name[i]] = yearning[i];
    return photo.map(x => x.reduce((p, c) => p + (dict[c] ?? 0), 0));
}