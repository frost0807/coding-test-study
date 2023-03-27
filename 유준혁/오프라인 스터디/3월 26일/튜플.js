function solution(s) {
    var answer = [];
    // 관리하기 편하게 배열 형태로 변경
    s = s.replaceAll('{', '[').replaceAll('}', ']');
    const array = JSON.parse(s);
    
    // 길이대로 정렬
    array.sort((a, b) => a.length - b.length)
        // 이전까지 없던 애를 결과 배열에 추가
        .forEach(x => {
            const n = x.filter(y => !answer.includes(y))[0];
            answer.push(n);
        })
    return answer;
}