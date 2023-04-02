function solution(s, answer = s.length, arr = [ ...s ]) {
    // 1개부터 s의 반까지 가능한 단위를 모두 확인
    // s의 반이 넘어간다면 압축이 불가능하므로 s의 길이와 동일해짐. 따라서 볼 필요 없음
    for(let i = 1; i <= s.length / 2; i++) {
        // size = i 개 단위로 압축했을 때 나오는 사이즈, strs = i 개 단위로 자른 문자열들
        let size = 0, strs = [];
        
        // i 개 단위로 잘라서 strs 에 넣기
        for(let j = 0; j < s.length; j += i) {
            strs.push(arr.slice(j, j + i).join(''));
        }
        
        // 압축 처리
        const press = strs.reduce((p, c) => {
            const last = p.at(-1);
            if (last[0] === c) last[1]++;
            else p.push([c, 1]);
            return p;
        }, [['', 1]]);
        
        // 길이 계산
        press.forEach(x => size += x[0].length + (x[1] > 1 ? x[1].toString().length : 0));
        
        // 갱신
        answer = Math.min(answer, size);
    }
    return answer;
}