/* Guppenmitglieder: ...... (bei Gruppenarbeit) */
import java.util.Scanner;

public class StringLengthSum {
  public static void main(String[] args) {
      
    Scanner sc = new Scanner(System.in);
    int index;
    int limit;
    int sum;
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
	int final_len = 0;
	for (int i=0; i< data.length; i++) {
		 final_len+=data[i].length();
	}

	System.out.printf("Total length of all lines is %d .",final_len);



/* Die folgenden Klammern müssen erhalten bleiben. */
  }
}
