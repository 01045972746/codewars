import java.util.*;
public class EnoughIsEnough {
    public static void main(String args[]) {
        int[] elements = new int[]{  1, 1, 3, 3, 7, 2, 2, 2, 2  };
        int maxOccurrences = 3;

       if(maxOccurrences == 0)
           System.out.println("Empty");
        List<Integer> intList = new ArrayList<Integer>();

        for (int p : elements) {
            if(intList.contains(p)) {
                if(Collections.frequency(intList, p) < maxOccurrences)
                    intList.add(p);
            }
            else intList.add(p);
        }

        int[] result = intList.stream().mapToInt(Integer::intValue).toArray();
    }
}
