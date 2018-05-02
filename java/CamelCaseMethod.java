import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class CamelCaseMethod {
    public static void main(String args[]) {
        String testCase = " camel case word";
        List<String> caseList = new ArrayList<String>(Arrays.asList(testCase.split(" ")));

        List<String> resultList = caseList.stream()
                .filter(p -> !p.equals(""))
                .map(p -> p.substring(0,1).toUpperCase() + p.substring(1))
                .collect(Collectors.toList());
        StringBuilder sb = new StringBuilder();
        for(String a: resultList) {
            sb.append(a);
        }

        System.out.println(sb.toString());

    }
}
