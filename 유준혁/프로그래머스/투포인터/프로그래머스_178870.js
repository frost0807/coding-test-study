// https://school.programmers.co.kr/learn/courses/30/lessons/178870
function solution(seq, k) {
    var answer = [], sum = 0, l = 0, r = 0, n = seq.length;
    while(l <= r && r < n) {
        sum += seq[r];
        if (sum >= k) {
            while(sum > k) {
                sum -= seq[l];
                l++;
            }
            if (sum === k) answer.push([l, r]);
        }
        r++;
    }
    return answer.sort((a, b) => {
        const adis = a[1] - a[0];
        const bdis = b[1] - b[0];
        return adis === bdis ? a[0] - b[0] : (adis - bdis);
    })[0];
}