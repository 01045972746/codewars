import java.util.*;
import java.util.stream.Collectors;

public class HighestScoringWord {
    public static void main(String args[]) {
        String str = "what time are we climbing up to the volcano";

        if(str.equals(""))
            return;
        List<String> strList = new ArrayList<>(Arrays.asList(str.split(" ")));
        Map<Character, Integer> alphaMap = new HashMap<Character, Integer>();
        Map<String, Integer> scoreMap = new HashMap<String, Integer>();
        int count = 1;
        for (char alpha='a'; alpha <= 'z'; alpha++) {
            alphaMap.put(alpha, count);
            count ++;
        }
        int max = Collections.max(strList.stream().map(p -> {
            char[] b = p.toCharArray();
            int score = 0;
            for(char k : b)
                score += alphaMap.get(k);
            scoreMap.put(p, score);
            return score;
        }).collect(Collectors.toList()));

        strList = strList.stream()
                .filter(p -> scoreMap.get(p) >= max)
                .collect(Collectors.toList());

        System.out.println(strList.get(0));
    }
}
