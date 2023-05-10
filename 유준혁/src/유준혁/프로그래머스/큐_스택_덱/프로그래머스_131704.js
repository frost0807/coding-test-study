// https://school.programmers.co.kr/learn/courses/30/lessons/131704?language=javascript
function solution(order, semi = [], x = 0) {
    for(let i = 1; i <= order.length; i++) {
        while(semi.length && semi.at(-1) === order[x]) (x++, semi.pop());
        if (i === order[x]) x++;
        else semi.push(i);
    }
    while(semi.length && semi.at(-1) === order[x]) (x++, semi.pop());
    return x;
}