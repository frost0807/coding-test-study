const ngram = (str) => {
    // arr = lowercase char 배열, map = 해시맵 처럼 사용할 객체
    const arr = [ ...str.toLowerCase()], map = {};
    return arr
        .map((x, i) => {
            // i, i + 1로 2-gram을 만듦
            const word = arr.slice(i, i + 2).join('');
            // 만들어진 word 끝에 동일한 word 중 몇 번째인지 붙여줌
            map[word] = (map[word] ?? 0) + 1;
            return word + map[word].toString();
         })
        // 조건에 맞도록 필터링 (영소문자 2글자 + index값 으로만 이루어져있는지)
        .filter(x => x.match(/[a-z]{2}[0-9]+/g));
}
function solution(str1, str2) {
    const n1 = ngram(str1), n2 = ngram(str2);
    // u = 합집합의 크기, n = 교집합의 크기
    const u = new Set([ ...n1, ...n2]).size, n = n1.filter(x => n2.includes(x)).length;
    // u가 0이라면 65536 바로 리턴
    if (!u) return 65536;
    return parseInt(n * 65536 / u);
}