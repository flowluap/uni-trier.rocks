/* Guppenmitglieder: ...... (bei Gruppenarbeit) */

import java.util.Scanner;
public class FirstLoop {
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int a;
    int b;
    int index;
    
    System.out.println("erste Eingabe: ");
    a = sc.nextInt();

    System.out.println("zweite Eingabe: ");
    b = sc.nextInt();

    while ( a <= b )
    {
      System.out.println( a );
      a+= + 1;
    }

/* Ab hier sollen Sie den Programmcode ergänzen */


/* Die zwei Klammern müssen erhalten bleiben! */
  }
}
