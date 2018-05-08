public class FindTheMissingLetter {
  public static void main(String args[]) {

      char[] t = new char[] { 'a','b','c','d','f' };
      int mem = 0;
      char l = '1';
      for(int i = 0 ; i < t.length; i++) {
          if(i == 0)
              mem = (int) t[i];
          else if(i < t.length){
              if((int) t[i] != mem+1) {
                  l = (char) (mem+1);
                  break;
              }
              else {
                  mem = mem+1;
              }

          }
      }
      System.out.println(l);
  }
}

// Clever
// public static char findMissingLetter(char[] array)
//   {
//     boolean stop = false;
//     int i;
//     for(i = 1; i < array.length && !stop; i++)
//     {
//       if (array[i] - array[i-1] != 1)
//         stop = true;
//     }
//     return (char) (array[i-1]-1);
//   }