const dateToInt = (date) => {
    const split = date.split('.').map(Number);
    return split[0] * 28 * 12 + split[1] * 28 + split[2];
}
function solution(today, terms, privacies) {
    today = dateToInt(today);
    let term = {};
    for(let t of terms) {
        const split = t.split(' ');
        term[split[0]] = Number(split[1]) * 28;
    }
    return privacies.map((x, idx) => {
        const split = x.split(' ');
        const day = dateToInt(split[0]) + term[split[1]];
        return today >= day ? idx + 1 : 0;
    }).filter(Boolean);
}