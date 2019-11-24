/* Guppenmitglieder: ...... (bei Gruppenarbeit) */
import java.util.Scanner;

public class StringLength {
  public static void main(String[] args) {
      
    Scanner sc = new Scanner(System.in);
    int index;
    int limit;
    String[] data;

/* Teil (a)  */

    System.out.println("Number of text lines:");
    limit = Integer.parseInt( sc.nextLine() );
    data = new String [limit];

/* Teil (b)  */

    System.out.println("Text lines:");
    index=0;
    while ( index < limit )
    {
      data[index] = sc.nextLine();
      index=index+1;
    }

/* Teil (c)  */

    System.out.println("Given input:");
    index = 0;
    while ( index < limit )
    {
      System.out.println("Line " + index + ": " + data[index]);
      index = index + 1;
    }

/* Teil (d): Ab hier Lösung der Aufgabe */

   System.out.println("Lengths of lines:");
    index = 0;
    while ( index < limit )
    {
      System.out.println("Line " + index + "has length " + data[index].length()+".");
      index = index + 1;
    }



/* Die folgenden Klammern müssen erhalten bleiben. */
  }
}
