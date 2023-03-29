const check = (arr, s, e) => {
    const mid = parseInt((s + e) / 2), isOne = arr[mid] === '1';
    if (s + 1 === e) return true;
    if (isOne) {
        const left = check(arr, s, mid), right = check(arr, mid + 1, e);
        return left && right;
    } else {
        for(let i = s; i < e; i++) {
            if (arr[i] === '1' && i !== mid) return false;
        }
    }
    return true;
}
function solution(numbers, answer = []) {
    for(var num of numbers) {
        let arr = [], binary = num.toString(2), n = 1, m = binary.length;
        while(binary.length > n - 1) n <<= 1;
        arr.length = n - 1;
        arr.fill(0);
        for(let i = 0; i < m; i++) arr[n - 2 - i] = binary[m - 1 - i];
        answer.push(check(arr, 0, n - 1) ? 1 : 0);
    }
    return answer;
}