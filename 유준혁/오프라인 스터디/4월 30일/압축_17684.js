function solution(msg, dict = {}, alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', idx = 1) {
    const answer = [];
    for(const a of [ ...alp ]) dict[a] = idx++; // 기본 사전 등록 (알파벳)
    for(let i = 0; i < msg.length;) {
        let word = msg[i], j = i + 1; // word = 현재 입력, j = i + 1 부터 탐색
        while(dict[word + msg[j]]) word += msg[j++]; // 다음 글자까지 추가했을 때 사전에 있는지 확인
        dict[word + msg[j]] = idx++; // 다음 글자 사전에 추가
        answer.push(dict[word]); // 현재 입력 결과에 추가
        i = j; // i값 다음 글자 index로 할당
    }
    return answer;
}