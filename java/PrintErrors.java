public class PrinterErrors {
    public static void main(String args[]) {
        String s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
        String ink = "abcdefghijklm";
        int count = 0;
        for(char k : s.toCharArray()) {
            if(ink.indexOf(k) == -1)
                count ++;
        }

        System.out.println(count+"/"+s.length());

    }
}

// Clever
// public class Printer {
    
//     public static String printerError(String s) {
//         return s.replaceAll("[a-m]", "").length() + "/" + s.length();
//     }
// }