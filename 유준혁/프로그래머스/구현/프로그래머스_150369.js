function solution(c, n, d, p) {
    var distance = 0;
    d = d.map((x, idx) => [x, idx + 1]).filter(x => x[0]);
    p = p.map((x, idx) => [x, idx + 1]).filter(x => x[0]);
    while(d.length || p.length) {
        let dpop = d.at(-1) ?? [0, 0], dc = c;
        let ppop = p.at(-1) ?? [0, 0], pc = c;
        const last = Math.max(dpop[1], ppop[1]);
        distance += last * 2;
        
        while(dc && d.length) {
            const min = Math.min(d.at(-1)[0], dc);
            d.at(-1)[0] -= min;
            dc -= min;
            if(!d.at(-1)[0]) d.pop();
        }
        while(pc && p.length) {
            const min = Math.min(p.at(-1)[0], pc);
            p.at(-1)[0] -= min;
            pc -= min;
            if(!p.at(-1)[0]) p.pop();
        }
    }
    return distance;
}