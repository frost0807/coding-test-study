let result = [], discount = [10, 20, 30, 40], users = [], emots = [];

// 구해진 할인율로 결과값 계산, result에 추가
const calc = (arr) => {
    const val = users.map(user => { // 모든 유저에 대해 확인
        let pay = 0, min = user[0], limit = user[1];
        arr.forEach((dis, idx) => {
            if (dis >= min) { // 구매 가능한 조건이면 할인율 적용하여 pay에 더함
                pay += emots[idx] - emots[idx] * (dis / 100);
            }
        });
        
        if (pay >= limit) return [1, 0]; // 상한과 같거나 크다면 플러스 가입
        else return [0, pay]; //아니면 금액 지불
    }).reduce((p, c) => [p[0] + c[0], p[1] + c[1]]); // 최종 결과로 합산
    result.push(val);
}

// 모든 할인 비율을 구하기 위한 함수
const permutation = (arr, idx) => {
    // 다 만들어졌다면 계산
    if (idx === arr.length) {
        calc(arr);
    } else {
        // arr[idx]에 할인율(10, 20, 30, 40)을 넣은 뒤 재귀 호출
        for(var i = 0; i < 4; i++) {
            let next = [ ...arr ];
            next[idx] = discount[i];
            permutation(next, idx + 1);
        }
    }
};

function solution(u, e) {
    users = u;
    emots = e;
    permutation(e.map(x => 0), 0); // e 길이만큼 0으로 채워진 배열과 idx 0부터 시작하는 permutation 호출
    // result 정렬하여 맨 앞 값 리턴
    return result.sort((a, b) => b[0] - a[0] === 0 ? b[1] - a[1] : b[0] - a[0])[0];
}