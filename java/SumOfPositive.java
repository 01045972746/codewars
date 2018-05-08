import java.util.OptionalInt;

import static java.util.Arrays.stream;

public class SumOfPositive {
    public static void main(String[] args) {
        int[] arr = new int[]{};

        OptionalInt sum = stream(arr).filter(p -> p > 0)
                .reduce((x, y) -> x + y);
        System.out.println(sum.isPresent() ? sum.getAsInt() : 0);
    }
}
