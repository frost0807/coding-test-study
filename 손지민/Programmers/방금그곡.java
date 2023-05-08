package 손지민.Programmers;

import java.util.ArrayList;
import java.util.List;

public class 방금그곡 {

    public int calcTime(String[] info) { // 재생시간 계산
        int startH = Integer.parseInt(info[0].substring(0, 2));
        int startM = Integer.parseInt(info[0].substring(3, 5));
        int endH = Integer.parseInt(info[1].substring(0, 2));
        int endM = Integer.parseInt(info[1].substring(3, 5));

        return (endH - startH) * 60 + (endM - startM);
    }

    public List<String> splitMusic(String musicStr) {
        List<String> music = new ArrayList<>();
        for(int i = 0; i < musicStr.length(); i++) {
            if(i + 1 < musicStr.length() && musicStr.charAt(i + 1) == '#') {
                music.add(musicStr.substring(i, i + 2));
                i += 1;
            }
            else music.add(musicStr.substring(i, i + 1));
        }
        return music;
    }


    public StringBuilder setMusicStr(int playTime, String musicStr, List<String> music) {
        StringBuilder sb = new StringBuilder();
        int cnt = playTime / music.size();
        int cnt2 = playTime % music.size();


        for(int i = 0; i < cnt; i++) sb.append(musicStr);
        for(int i = 0; i < cnt2; i++) sb.append(music.get(i));

        return sb;
    }

    public boolean isFind(StringBuilder musicStr, String mStr) {
        if(musicStr.length() < mStr.length()) return false;

        List<String> music = splitMusic(musicStr.toString());
        List<String> m = splitMusic(mStr);

        for(int i = 0; i < music.size(); i++) {
            if(music.get(i).equals(m.get(0))) {
                int index = i;
                boolean isOk = true;
                for(int j = 0; j < m.size(); j++) {
                    if(index >= music.size() || !music.get(index).equals(m.get(j)) ){
                        isOk = false;
                        break;
                    }
                    index += 1;
                }
                if(isOk) return true;
            }
        }

        return false;
    }


    public String solution(String m, String[] musicinfos) {
        String res = "(None)";
        int resTime = 0;

        for(String musicinfo : musicinfos) {
            String[] info = musicinfo.split(",");

            int playTime = calcTime(info);
            List<String> music = splitMusic(info[3]);
            StringBuilder sb = setMusicStr(playTime, info[3], music);

            if(isFind(sb, m) && playTime > resTime)  {
                res = info[2];
                resTime = playTime;
            }
        }

        return res;
    }
}