/* Guppenmitglieder: ...... (bei Gruppenarbeit) */
import java.util.Scanner;
public class SimpleModification {
  public static void main(String[] args) {
  /*  Dieses Programm liest im Original von der Konsole zwei Zahlen ein
  und berechnet daraus die Summe und die Differenz der eingegebenen Zahlen.  */
      
    Scanner sc = new Scanner(System.in);
    int    ersteZahl;
    int    zweiteZahl;
    int    ergebnis;
    
    System.out.println("erste Eingabe: ");
    ersteZahl = sc.nextInt();

    System.out.println("zweite Eingabe: ");
    zweiteZahl = sc.nextInt();

    ergebnis    =  ersteZahl * 3;
    System.out.println("erstes Resultat: " + ergebnis);

    ergebnis    =  zweiteZahl + ersteZahl * 2;
    System.out.println("zweites  Resultat: " + ergebnis);

/*
Modifizieren Sie die Zeilen 20 und 23 im obigen Programmteil so, 
dass das Programm statt der Summe und der Differenz der Zahlen
- bei Zeile 21 das Dreifache der ersten Zahl ausgibt und 
- bei Zeile 24 die Summe aus der zweiten Zahl und dem Doppelten 
  der ersten Zahl ausgibt..
*/
  }
}
