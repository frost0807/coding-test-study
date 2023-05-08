const tti = (str) => Number(str.split(':')[0]) * 60 + Number(str.split(':')[1]) // time to int
const ito = (info, i) => { // info to object
    const split = info.split(',');
    const start = tti(split[0]), end = tti(split[1]), title = split[2];
    const playtime = end - start, melody = split[3].match(/[A-Z]{1}[#]?/g);
    const timeline = []; // 재생시간 동안 플레이 된 멜로디를 모아놓음
    for(let i = 0; i < end - start; i++) timeline.push(melody[i % melody.length]);
    
    return { id: i, start, end, title, playtime, melody, timeline };
}

function solution(m, musicinfos) {
    let melody = m.match(/[A-Z]{1}[#]?/g); // CC#BCC#BCC#BCC#B > ['C', 'C#', 'B', 'C', 'C#', 'B' ...]
    let infos = musicinfos.map((info, i) => ito(info, i));
    
    // 검색
    let search = infos.filter(info => {
        let find = false, timeline = info.timeline;
        // timeline에서 melody와 정확히 일치하는 연속된 부분 배열이 있는지 체크
        for(let i = 0; i < info.playtime - melody.length + 1 && !find; i++) {
            find |= melody.every((x, idx) => x === timeline[idx + i]);
        }
        return find;
    })
    // 이후 조건에 맞게 정렬
    .sort((a, b) => {
        // 재생 시간 긴 음악 우선
        if (a.playtime !== b.playtime) return b.playtime - a.playtime;
        // 아닐 경우 먼저 입력된 순서
        return a.id - b.id;
    });
    return search[0]?.title ?? '(None)'; // optional operator로 처리
}