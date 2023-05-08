const wh = [[0, 1, 0, -1], [1, 0, -1, 0]];
const isClear = (board) => board.flat(1).every(x => !x);
let vst = {};
const state = (board, r, c) => [ ...board.flat(1), r, c ].join(',');
const move = (board, r, c, d, max) => {
    const rst = [ r, c ];
    while(max--) {
        const nr = rst[0] + wh[0][d], nc = rst[1] + wh[1][d];
        if (0 <= nr && 0 <= nc && nr < 4 && nc < 4) {
            rst[0] = nr;
            rst[1] = nc;
            if (board[nr][nc] > 0) break;
        } else break;
    }
    return rst;
}
const enter = (board, r, c) => {
    const idx = board.flat(1).findIndex(x => x < 0);
    if (idx < 0) board[r][c] *= -1;
    else {
        const a = parseInt(idx / 4), b = idx % 4;
        if (board[a][b] + board[r][c] !== 0) {
            board[a][b] *= -1;
        } else {
            board[r][c] = 0;
            board[a][b] = 0;
        }
    }
}
const copy = (board) => [ ...board.map(x => [ ...x ]) ];
function solution(board, r, c, i = 0) {
    const q = [];
    q.push([copy(board), r, c, 0]);
    while(i < q.length) {
        let [board, r, c, cnt] = q[i++];
        if (isClear(board)) return cnt;
        else {
            for(let i = 0; i < 8; i++) {
                const [nr, nc] = move(board, r, c, i % 4, 4 ** parseInt(i / 4));
                const st = state(board, nr, nc);
                if (!vst[st]) {
                    vst[st] = cnt + 1;
                    q.push([ copy(board), nr, nc, cnt + 1 ]);
                }
            }
            if (board[r][c] !== 0) {
                const cboard = copy(board);
                enter(cboard, r, c);
                const st = state(cboard, r, c);
                if (!vst[st]) {
                    vst[st] = cnt + 1;
                    q.push([ cboard, r, c, cnt + 1 ]);
                }
            }
        }
    }
    return -1;
}