/* Guppenmitglieder: ...... (bei Gruppenarbeit) */

public class SimpleLoopModification {
  public static void main(String[] args) {
      
    int index;
    int limit;

/* Nur drei der Zeilen 10 bis 17 sollen verändert werden: */
    index =  1;
    limit = 5;

    while ( index <= limit )
    {
      System.out.println( index + ". Zeile");
      index = index + 1;
    }
  }
}
