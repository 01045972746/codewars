public class SumOfTheFirstnthTermOfSeries {
    public static void main(String args[]) {
        System.out.println(
                (double)1 + (double)1/(double)4 + (double)1/(double)7 + (double)1/(double)10 + (double)1/(double)13
        );
        double a = 0.00;
        for(int i = 1; i < 6; i++) {
            a += (double)1 / (double)(3*i-2);
        }
        System.out.println(Math.round(a*100)/100.0);
    }
}
