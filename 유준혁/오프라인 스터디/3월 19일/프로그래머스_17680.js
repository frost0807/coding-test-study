function solution(cacheSize, cities, cache = []) {
    let time = 0;
    cities
        .map(x => x.toLowerCase()) // 대소문자 구분 X
        .forEach(x => { // cities를 순회
            time += cache.find(c => c === x) ? 1 : 5; // 캐시힛 = 1, 미스 = 5
            cache = cache.filter(c => x !== c); // LRU 적용
            cache.push(x);
            if (cache.length > cacheSize) cache.shift(); // 캐시 사이즈 유지
        });
    return time;
}