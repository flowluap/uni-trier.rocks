/* Guppenmitglieder: ...... (bei Gruppenarbeit) */
import java.util.Scanner;

public class PaperChase {
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int index;
    int limit;   
    int count;
    int[] data;
    
/* In den folgenden Bereich soll die Lösung eingesetzt werden: */
	index = 0;
	
	System.out.println("How many numbers:");
    limit = Integer.parseInt( sc.nextLine() );
    data = new int [limit];
    
    System.out.printf("\n %d numbers: \n",limit);
	for (int i=0; i < limit; i++) {
		 data[i] = sc.nextInt();
	}
	for (int i=0; i < 10; i++) {
		
		System.out.print(index);
		index = data[index];
		
		
		
	}



/* Die Klammern müssen bleiben */
  }
}
