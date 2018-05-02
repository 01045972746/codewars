import java.util.*;

public class GroupWord {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int c = 0;

        List<String> abc = new ArrayList<>();

        while(c <= a) {
            abc.add(sc.nextLine());
            c++;
        }

        Map<Character, Boolean> bMap = new HashMap<>();
        int result_count = 0;
        for(String p: abc) {
            char[] k = p.toCharArray();
            for(char t: k) {
                if(bMap.get(t) != null) {
                    bMap.put(t, true);
                    result_count ++;
                }
                else
                    break;
            }
            bMap.clear();
        }

        System.out.println(result_count);
    }
}
