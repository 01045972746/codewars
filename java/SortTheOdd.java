import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import static java.util.Arrays.stream;

public class SortTheOdd {
    public static void main(String args[]) {
        int[] array = new int[]{ 5, 3, 2, 8, 1, 4 };


        List<Integer> oddList = stream(array).boxed().collect(Collectors.toList());
        List<Integer> oddIndexList = new ArrayList<>();
        oddList = oddList.stream().filter(p -> p % 2 != 0).collect(Collectors.toList());
        Collections.sort(oddList);
        for(int i = 0 ; i < array.length; i ++) {
            if(array[i] % 2 != 0)
                oddIndexList.add(i);
        }

        for(int i = 0 ; i < oddIndexList.size(); i ++)
            array[oddIndexList.get(i)] = oddList.get(i);


    }
}

//Clever
// // Sort the odd numbers only
// final int[] sortedOdd = Arrays.stream(array).filter(e -> e % 2 == 1).sorted().toArray();

// // Then merge them back into original array
// for (int j = 0, s = 0; j < array.length; j++) {
//   if (array[j] % 2 == 1) array[j] = sortedOdd[s++];
// }

// return array;