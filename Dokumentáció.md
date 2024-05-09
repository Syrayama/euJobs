**BackTrack osztály**

A "BackTrack" osztályban van megvalósítva az egyik megoldó algoritmus, a BackTrack. Az osztály egy visszalépéses (backtracking) kereső algoritmust implementál a gyümölcsök cseréjének problémájára. A "BackTrack" osztály a "GráfKereső" absztrakt osztályból származik, és rekurzív megközelítést alkalmaz a probléma megoldására. A visszalépéses keresés ki van egészítve mélységi korlátozással és emlékezetes, ami annyit jelent, hogy figyeli, hogy volt-e már abban az állapotban amibe most belép, ezzel megvalósítva a körfigyelést.

**Osztálydefiníció:**

 * Osztálynév: BackTrack
 * Szülőosztály: GráfKereső

**Adattagok:**

 * korlát: A keresés mélységi korlátja (int típus). Ha 0, akkor nincs korlát beállítva.
 * emlékezetes: Körfigyelés aktiválására szolgáló logikai érték. Ha igazra állítjuk, akkor a keresés körfigyelést alkalmaz.

**Konstruktorok:**

 * BackTrack(Csúcs startCsúcs, int korlát, bool emlékezetes): Beállítja a kezdőcsúcsot, a mélységi korlátot, és az emlékezetes keresési módot.
 * További konstruktorok állnak rendelkezésre különböző paraméterekkel, például csak korláttal, vagy csak emlékezetes mód beállításával.
   * public BackTrack(Csúcs startCsúcs, int korlát) : this(startCsúcs, korlát, false) { } - Ha ezt a konstruktort hívjuk, akkor csak mélységi korlát lesz, a körfigyelés hamis értékre lesz állítva.
   * public BackTrack(Csúcs startCsúcs, bool emlékezetes) : this(startCsúcs, 0, emlékezetes) { } - Ha ezt a kontruktort hívjuk, akkor nem lesz mélységi korlát, de lesz körfigyelés, mivel igaz-ra van állítva.

**Metódusok:**

 * Keresés(): A keresési folyamat kezdetét jelenti. A metódus a kezdőcsúcsból indul, és rekurzív módon hívja magát az aktuális csúcsokon keresztül. Egy terminális csúcsot ad vissza, ha nincs ilyen, akkor null értéket ad vissza.

 * Keresés(Csúcs aktCsúcs): A rekurzív keresés megvalósítása. Mivel rekurzív, ezért a visszalépésnek a "return null" felel meg.
     A metódus az aktuális csúcsból indul, és a következő lépéseket hajtja végre:
   1. Ellenőrzi a mélységi korlátot. Ha a mélység eléri a korlátot, visszalépés történik (null értékkel tér vissza).
   2. Ha az emlékezetes mód aktív, akkor a szülőkön keresztül ellenőrzi, hogy az aktuális állapotot korábban már vizsgáltuk-e.
   3. Ellenőrzi, hogy az aktuális csúcs célállapot-e (azaz a probléma megoldása). Ha igen, visszaadja ezt a csúcsot mint megoldást.
   4. Ha nem célállapot, akkor az összes lehetséges operátort végigpróbálja az aktuális állapoton, új csúcsokat generálva.
   5. Az új csúcsokra rekurzívan meghívja a Keresés metódust.
   6. Ha egy új csúcs vezet megoldáshoz, a terminális csúcsot visszaadja. Ha nem, a következő operátort próbálja ki.
   7. Ha az összes operátor kipróbálása után sem talál megoldást, null értékkel tér vissza.

***Összefoglaló:***

A "BackTrack" osztály egy hatékony rekurzív keresési megoldást implementál a gyümölcsök cseréje problémájához, kihasználva a visszalépéses algoritmus (backtracking) előnyeit, mint a mélységi korlát és az emlékezetes keresés. Az osztály központi szerepet tölt be a gyümölcsök cseréjével kapcsolatos probléma megoldásában, lehetővé téve a különböző állapotok közötti navigálást a célállapot eléréséig.
