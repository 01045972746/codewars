import java.util.stream.IntStream;

public class BrokenSequence {
    public static void main(String args[]) {
        String str = "1 3 2 5";
        String[] strings = str.split(" ");

        int[] intArr = new int[strings.length];
        for(int i = 0; i < intArr.length; i++) {
            try {
                intArr[i] = Integer.parseInt(strings[i]);
            }
            catch(NumberFormatException e) {
                return;
            }
        }
            int sum = IntStream.of(intArr).sum();
            int max = IntStream.of(intArr).max().getAsInt();
            System.out.println((1+max) * max / 2 - sum);
    }
}
