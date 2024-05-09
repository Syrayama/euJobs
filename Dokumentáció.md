**DOKUMENTÁCIÓ**

A program azt a problémát/feladatot hivatott megoldani, hogy van 13 almánk, 46 körténk és 59 barackunk, a csősszel cserélgetünk és 2 különböző gyümölcsért ad a harmadik fajtából kettőt.

1. --- **GyümölcsökÁllapot osztály** ---

Az állapottér a "GyümölcsökÁllapot" osztály, ami az "AbsztraktÁllapot" absztrakt osztályt valósítja meg, ami a különböző állapotok kezelését teszi lehetővé.
Az osztály felelőssége, hogy kezelje a gyümölcsök állapotait (alma, körte, barack) és végrehajtsa az állapotok közti átmeneteket. Az operátorok egyszerűsége és száma végett a jegyzet alapján az operátorok is ebben az osztályban lettek implementálva.

**Osztálydefiníció:**

 *    Osztálynév: GyümölcsökÁllapot
 *    Szülőosztály: AbsztraktÁllapot

**Adattagok:**

 *    alma: A nálunk lévő almák számát tárolja (int típusban).
 *    körte: A nálunk lévő körték számát tárolja (int típusban).
 *    barack: A nálunk lévő barackok számát tárolja (int típusban).

**Konstruktor:**

 *    GyümölcsökÁllapot(int alma, int körte, int barack): Beállítja a nálunk lévő gyümölcsök kezdeti számát.

**Metódusok:**

 *    CélÁllapotE(): A kívánt célállapot vizagálatára van. Igaz értéket ad vissza, ha csak egy típusú gyümölcs van, ami nem nulla. Ez azt jelenti, hogy vagy csak almák, csak körték, vagy csak barackok maradtak nálunk. Ez a feladatban leírt kívánt eredmény állapota.

 *    ÁllapotE(): Azt ellenőrzi, hogy egyáltalán elfogadható állapot-e a paraméterként kapott érték. Igazat ad vissza, ha minden gyümölcs száma egyenlő vagy nagyobb, mint 0. Ellenőrzi, hogy a gyümölcsök száma logikailag helyes-e a feladat leírása szerint.

 *    PreGyümölcsCsere(int gyümölcs1, int gyümölcs2): Előfeltétel. Segédfüggvény a gyümölcsök cseréjének előkészítésére. Igazat ad vissza, ha mindkét gyümölcs száma nagyobb, mint 0.

 *    GyümölcsCsere(int gyümölcs1, int gyümölcs2, int gyümölcs3): Operátor. Végrehajt egy cserét a megadott gyümölcsök között. Az operátor csökkenti az első két gyümölcs mennyiségét eggyel, és növeli a harmadik gyümölcs mennyiségét kettővel. If és else if ágakkal felírva a 3 lehetséges kimenet.

 *    SzuperOperátor(int i): Egy átfogó operátor, amely az alapoperátorokat valósítja meg. Visszaadja az eredményt az adott operátor alkalmazásáról. Ezen keresztül lehet elérni az összes operátort. Igazat ad vissza, ha az i.dik alap operátor alkalmazható a belső állapotra. Case-ekkel vannak megvílósítva a lehetőségek.

 *    OperátorokSzáma(): Visszaadja az alkalmazható operátorok számát, jelen esetben 3.

 *    ToString(): A ToString metódus felülírása, hogy alapvetően a nekünk megfelelő formátumban íródjanak ki az adatok.

 *    Equals(): Mivel emlékezetes backtracket és mélységi keresést használok felül kellett írni az Equals-t is a megfelelő összehasonlításhoz.

 *    GetHashCode(): Az Equals felülírása miatt szükséges, mert ha két példány egyenlő, akkor a hash kódjuk is egyenlő.

 *    A Clone metódust nem kellett felülírni az osztályban, mert a tárolt adatok típusa miatt elég az ősosztályban megvalósított sekély klónozás ( MemberwiseClone() ).

***Összefoglalás:***

A GyümölcsökÁllapot osztály a gyümölcsök csere algoritmus állapotainak kezelését teszi lehetővé. Ez az állapottér. Magában foglalja a gyümölcsök számának nyomon követését, valamint az állapot-átmenetek (cserék) kezelését. A célállapot elérése, azaz amikor csak egy típusú gyümölcs marad, a megoldás célja. Az osztály szorosan kapcsolódik a problémamegoldás logikájához, és szerves része a teljes megoldási folyamatnak. Az operátorok iside kerültek felvételre.

-----------------------------

2. --- **BackTrack osztály** ---

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
2. Ha az emlékezetes mód aktív, akkor a szülőkön keresztül ellenőrzi, hogy az aktuális állapotot korábban már vizsgálta-e.
3. Ellenőrzi, hogy az aktuális csúcs célállapot-e (azaz a probléma meg van-e oldva). Ha igen, visszaadja ezt a csúcsot megoldásként.
4. Ha az aktuális állapot nem célállapot, akkor az összes lehetséges operátort végigpróbálja az aktuális állapoton, új csúcsokat generálva.
5. Az új csúcsokra rekurzívan meghívja a Keresés metódust.
6. Ha egy új csúcs vezet megoldáshoz, a terminális csúcsot adja vissza, haa nem, akkor a következő operátort próbálja.
7. Ha az összes operátor kipróbálása után sem talál megoldást, null értékkel tér vissza.

***Összefoglalás:***

A "BackTrack" osztály egy hatékony rekurzív keresési megoldást implementál a gyümölcscsere problémához, kihasználva a visszalépéses algoritmus előnyeit, mint a mélységi korlát és az emlékezetes keresés. Az osztály központi szerepet tölt be a gyümölcsök cseréjével kapcsolatos probléma megoldásában, lehetővé téve a különböző állapotok közötti navigálást a célállapot eléréséig.

-----------------------------

3. --- **MélységiKeresés osztály** ---

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

-----------------------------

4. --- **A megoldó algoritmusok hatékonyságai** ---

A megoldás lépésszámai több lefuttatásnál is ugyanazok.  
Az emlékezetes, 50-es mélységi korlátos BackTrack 46 lépésből oldja meg, míg a Mélységi keresés körfigyeléssel 1339 lépésből.

**Két algoritmus futási ideje:**

***Emlékezetes BackTrack 50-es mélységi korláttal és Mélységi keresés körfigyeléssel***
 * Megoldási idők másodpercben (BackTrack -- Mélységi):

1. 0,0161 -- 0,4422
2. 0,0052 -- 0,3692
3. 0,0034 -- 0,5153
4. 0,0033 -- 0,5554
5. 0,0029 -- 0,2203
6. 0,0032 -- 0,1780
7. 0,0034 -- 0,2683
8. 0,0036 -- 0,2469
9. 0,0060 -- 0,1724
10. 0,0052 -- 0,2942

Ebből látható, hogy a BackTrack algoritmus a kiegészítésekkel ennél a feladatnál hatékonyabbnak bizonyul.
