function solution(data, col, row_begin, row_end) {
    return data.sort((a, b) => a[col - 1] - b[col - 1] === 0 ? b[0] - a[0] : a[col - 1] - b[col - 1])
        .map((x, idx) => {
            const mod = x.reduce((p, c) => p + (c % (idx + 1)), 0);
            if (row_begin - 1 <= idx && idx <= row_end - 1) return mod;
            return 0;
        })
        .reduce((p, c) => p ^ c);
}