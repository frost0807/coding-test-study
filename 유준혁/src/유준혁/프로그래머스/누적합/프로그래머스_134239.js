function solution(k, ranges) {
    const sum = [0], K = k;
    while(k > 1) {
        if (k % 2 == 0) (sum.push(k * 3 / 4 + sum.at(-1)), k /= 2);
        else (sum.push((k + k * 3 + 1) / 2 + sum.at(-1)), k = k * 3 + 1);
    }
    return ranges.map(x => {
        const l = x[0], r = sum.length + x[1] - 1;
        if (r < l) return -1;
        return sum[r] - sum[l];
    });
}