**BackTrack osztály**

Az alábbi dokumentáció a "BackTrack" osztályra vonatkozik, amely egy visszalépéses (backtracking) kereső algoritmust implementál a gyümölcsök cseréjének problémájára. A "BackTrack" osztály a "GráfKereső" absztrakt osztályból származik, és rekurzív megközelítést alkalmaz a probléma megoldására.

**Osztálydefiníció:**

 * Osztálynév: BackTrack
 * Szülőosztály: GráfKereső

**Adattagok:**

 * korlát: A keresés mélységi korlátja (integer). Ha 0, nincs korlát beállítva.
 * emlékezetes: Körfigyelés aktiválására szolgáló logikai érték. Ha igaz, a keresés körfigyelést alkalmaz.

**Konstruktorok:**

 * BackTrack(Csúcs startCsúcs, int korlát, bool emlékezetes): Beállítja a kezdőcsúcsot, a mélységi korlátot, és az emlékezetes keresési módot.
 * További konstruktorok állnak rendelkezésre különböző paraméterekkel, például csak korláttal, vagy csak emlékezetes mód beállításával.

**Metódusok:**

 * Keresés(): A keresési folyamat kezdetét jelenti. A metódus a kezdőcsúcsból indul, és rekurzív módon hívja magát az aktuális csúcsokon keresztül.

 * Keresés(Csúcs aktCsúcs): A rekurzív keresés megvalósítása.
       A metódus az aktuális csúcsból indul, és a következő lépéseket hajtja végre:
        Ellenőrzi a mélységi korlátot. Ha a mélység eléri a korlátot, visszalépés történik (null értékkel tér vissza).
        Ha az emlékezetes mód aktív, akkor a szülőkön keresztül ellenőrzi, hogy az aktuális állapotot korábban már vizsgáltuk-e.
        Ellenőrzi, hogy az aktuális csúcs célállapot-e (azaz a probléma megoldása). Ha igen, visszaadja ezt a csúcsot mint megoldást.
        Ha nem célállapot, akkor az összes lehetséges operátort végigpróbálja az aktuális állapoton, új csúcsokat generálva.
        Az új csúcsokra rekurzívan meghívja a Keresés metódust.
        Ha egy új csúcs vezet megoldáshoz, a terminális csúcsot visszaadja. Ha nem, a következő operátort próbálja ki.
        Ha az összes operátor kipróbálása után sem talál megoldást, null értékkel tér vissza.

***Összefoglaló:***

A "BackTrack" osztály egy hatékony rekurzív keresési megoldást implementál a gyümölcsök cseréje problémájához, kihasználva a visszalépéses algoritmus (backtracking) előnyeit, mint a mélységi korlát és az emlékezetes keresés. Az osztály központi szerepet tölt be a gyümölcsök cseréjével kapcsolatos probléma megoldásában, lehetővé téve a különböző állapotok közötti navigálást a célállapot eléréséig.
