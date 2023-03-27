const points = [];
const dfs = (n, idx, info, rst) => {
    // 중간에 n이 0보다 작아질 수 있음 (info[idx] + 1이 n보다 큰 경우)
    if (n < 0) return;
    // 모든 화살을 다 쓴 경우
    if (n === 0) {
        let isum = 0, rsum = 0;
        // 점수차 구하기
        for(var i in info) {
            if (info[i] + rst[i] === 0) continue;
            if (info[i] >= rst[i]) isum += 10 - i;
            else rsum += 10 - i;
        }
        
        if (rsum > isum) {
            // 과녁 맞힌 방법과 점수차를 points에 추가함
            points.push([ ...rst, rsum - isum]);
        }
    } else {
        // n이 남아있는 경우 idx가 11 이상 갈 수 있기 때문에 idx확인처리
        if (idx < 11) {
            // 화살을 쏘는 방법은 총 3가지
            // 0 = 이번 과녁은 포기
            // info[idx] + 1 = 점수 획득
            // n = 남은 화살 모두 소비
            const arrows = [ 0, info[idx] + 1, n ];
            for(const arrow of arrows) {
                let temp = [ ...rst ];
                temp[idx] = arrow;
                // 위 방법들에 대하여 재귀적으로 탐색 수행
                dfs(n - arrow, idx + 1, info, temp);
            }
        }
    }
}
function solution(n, info) {
    var answer = [];
    // 모든 방법에 대해 DFS 탐색 수행
    dfs(n, 0, info, info.map(x => 0));
    // 점수차 desc, 낮은 점수 desc 로 정렬
    points.sort((a, b) => {
        // 점수차 먼저 확인
        if (b.at(-1) - a.at(-1)) return b.at(-1) - a.at(-1);
        
        // 점수차가 동일하다면 낮은 점수를 많이 맞힌 쪽으로
        for(let i = 10; i >= 0; i--) {
            if(a[i] !== b[i]) return b[i] - a[i];
        }
        return 0;
    });
    
    // 이긴 방법이 있다면 내림차순 정렬의 맨 앞, 아니라면 [ -1 ]
    return points.length ? points[0].slice(0, 11) : [-1];
}