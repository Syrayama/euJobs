**DOKUMENTÁCIÓ**

A program azt a problémát/feladatot hivatott megoldani, hogy van 13 almánk, 46 körténk és 59 barackunk, a csősszel cserélgetünk és 2 különböző gyümölcsért ad a harmadik fajtából kettőt.

---**GyümölcsökÁllapot osztály**---

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
