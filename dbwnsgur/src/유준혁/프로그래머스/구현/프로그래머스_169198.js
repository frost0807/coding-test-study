function solution(m, n, x, y, balls) {
    return balls.map(([a, b]) => {
        let left = (x + a) ** 2 + Math.abs(b - y) ** 2
            , right = (m * 2 - (x + a)) ** 2 + Math.abs(b - y) ** 2
            , top = (y + b) ** 2 + Math.abs(a - x) ** 2
            , bottom = (n * 2 - (y + b)) ** 2 + Math.abs(a - x) ** 2
            , max = 1 << 30;
        if (x === a) {
            if (y < b) bottom = max;
            else top = max;
        }
        if (y === b) {
            if (x < a) right = max;
            else left = max;
        }
        return Math.min(left, right, top, bottom);
    });
}