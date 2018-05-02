import java.util.List;
import java.util.stream.Collectors;

import static java.util.Arrays.stream;

public class OddOrEven {
    public static void main(String args[]) {
        int[] a = new int[] {2, 5, 34, 6};
        int[] an = stream(a).map(p -> p *2).toArray();

        for(int i: an)
            System.out.println(i);
    }
}
