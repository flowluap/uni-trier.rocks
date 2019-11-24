/* Wie kann man denn so ekelhaften Code schreiben?! */

import java.util.Scanner;
public class FirstArray {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int index, limit;
    String[] array;

    limit = 5;
    array = new String[limit];

    System.out.println( limit + " lines of input, please:");
    
/* Änderungen nur im folgenden Bereich! */

    index=4;
    while (index != -1) {
      array[index] = sc.nextLine();
      index-=1;
    }

/* Ab hier sind keine Änderungen mehr erlaubt! */

    System.out.println( "Output: ");
    index = 0;
    while (index < limit) {
      System.out.println( array[index]);
      index = index + 1;
    }
  }
}
