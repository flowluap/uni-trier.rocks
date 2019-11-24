/* Guppenmitglieder: ...... (bei Gruppenarbeit) */
import java.util.Scanner;

public class Uebung03_A1 {
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int index;
    int anzahl;
    int[] feld;
    int maximalwert;
    
    anzahl = sc.nextInt();
    feld = new int[anzahl];

    index = 0;
    while ( index < anzahl )
    {
      feld[index] = sc.nextInt();
      index = index + 1;
    }
<<<<<<< HEAD
    
    
/* Loesung ab hier ----------------*/ 
/* (a) Vorbereitung der Suche      */
	System.out.println("How many numbers:");
    limit = Integer.parseInt( sc.nextLine() );
    data = new int [limit];
    
    System.out.printf("\n %d numbers: \n",limit);
	for (int i=0; i < limit; i++) {
		 data[i] = sc.nextInt();
	}

/* (b) eigentliche Suche           */

	maximalwert=data[0]; /*negativ numbers*/
	
	for (int i=0; i < limit; i++) {
		
		if (data[i] > maximalwert){
			maximalwert = data[i];
		}

	}

/* (c) Auswertung                  */

System.out.printf("\n Highest number: %d \n",maximalwert);

