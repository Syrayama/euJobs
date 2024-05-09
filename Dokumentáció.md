**MélységiKeresés osztály**

A "MélységiKeresés" osztály a mélységi keresés algoritmust implementálja a gyümölcsök cseréjének problémájára. Az osztály a "GráfKereső" absztrakt osztályból származik, és az állapotok közötti navigálásra és a célállapot elérésére szolgál.

**Osztálydefiníció:**

 * Osztálynév: MélységiKeresés
 * Szülőosztály: GráfKereső

**Adattagok:**

 * Nyilt: A még nem kiterjesztett csúcsokat tároló verem. Mélységi keresés esetén ez segít abban, hogy mindig a legmélyebb, még nem vizsgált csúcsot vehessük elő. Kezdetben csak a start csúcs nyílt.
 * Zárt: A már kiterjesztett csúcsok halmazát tároló lista. Ez segít a már feldolgozott csúcsok nyomon követésében. Kezdetben a zárt csúcsok halmaza üres.
 * körFigyelés: Egy logikai érték, amely meghatározza, hogy a keresés során legyen-e körfigyelés. Ha igaz, a keresés kiszűri azokat az útvonalakat, amelyeken már járt az algoritmus.

**Konstruktorok:**

 * MélységiKeresés(Csúcs startCsúcs, bool körFigyelés): Inicializálja a keresést a megadott kezdőcsúccsal és beállítja a körfigyelést.
 * MélységiKeresés(Csúcs startCsúcs): Alapértelmezés szerint bekapcsolja a körfigyelést.

**Metódusok:**

 * Keresés(): Elindítja a keresési folyamatot. A keresési logika a körfigyelés beállításától függ. Ha a körfigyelés be van kapcsolva, a TerminálisCsúcsKeresés() metódust használja, egyébként a TerminálisCsúcsKeresésGyorsan() metódust, ami gyorsabb, ha nem szükséges a körfigyelés, azonban ha kell a körfigyelés, akkor ez a módszer nem megfelelő, mert cégtelen ciklusba eshet.

 * TerminálisCsúcsKeresés(): A mélységi keresést valósítja meg, figyelve a köröket. Amíg van nyílt csúcs, kiveszi a verem tetejéről a csúcsot, kiterjeszti az új csúcsokkal, és ezeket hozzáadja a nyíltakhoz, ha még nem szerepeltek a nyílt vagy zárt halmazban. Ha talál célállapotot, visszatér ezzel a csúccsal.

 * TerminálisCsúcsKeresésGyorsan(): Hasonló a TerminálisCsúcsKeresés()-hez, de nem figyeli a köröket, így gyorsabb, de kockázatosabb, mert végtelen ciklust okozhat.

***Összefoglaló:***

A "MélységiKeresés" osztály egy hatékony eszköz a gyümölcscsere problémájának megoldására mélységi keresés segítségével. Az osztály képes kezelni a köröket a körfigyelési opcióval, ami biztosítja, hogy a keresés ne ragadjon be ismétlődő ciklusokba. A különböző konstruktorok és a két különböző keresési módszer lehetővé teszi, hogy a környezetnek megfelelően lehessen optimalizálni a keresést.
