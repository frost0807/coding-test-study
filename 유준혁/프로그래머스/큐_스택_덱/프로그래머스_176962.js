// https://school.programmers.co.kr/learn/courses/30/lessons/176962?language=javascript
const tti = (time) => time.split(':').map(Number).map((x, idx) => x * Math.pow(60, 1 - idx)).reduce((p, c) => p + c);
function solution(plans, last, stack = [], answer = []) {
    plans = plans.map(x => (x[1] = tti(x[1]), x)).sort((a, b) => a[1] - b[1]);
    while(plans.length) {
        let plan = plans.shift(), time = plan[1], left = time - last;
        while(stack.length && left) {
            const min = Math.min(stack.at(-1)[2], left);
            stack.at(-1)[2] -= min;
            left -= min;
            if (!stack.at(-1)[2]) answer.push(stack.pop()[0]);
        }
        last = time;
        stack.push(plan);
    }
    return [ ...answer, ...stack.sort((a, b) => -1).map(x => x[0])];
}