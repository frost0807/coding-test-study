function solution(e, starts, cnt = [0]) {
    for(let i = 1; i <= e; i++) {
        for(let j = i; j <= e; j += i) {
            cnt[j] = (cnt[j] ?? 0) + 1;
        }
    }
    cnt = cnt.map((x, idx) => [x, idx]).sort((a, b) => a[0] - b[0] === 0 ? a[1] - b[1] : b[0] - a[0]);
    return starts.map(x => {
        let max = 0;
        for(let arr of cnt) {
            if (x <= arr[1] && arr[1] <= e) {
                max = arr[1];
                break;
            }
        }
        return max;
    });
}