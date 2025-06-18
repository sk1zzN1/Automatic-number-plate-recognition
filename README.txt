README - Aplicatie OCR pentru Numere Auto

Aceasta aplicatie permite recunoasterea automata a numerelor de inmatriculare din imagini si clasificarea lor dupa liste prestabilite.

────────────────────────────────────────────
CUM SE FOLOSESTE APLICATIA
────────────────────────────────────────────

1. Descarca folderul complet care contine:
   - app.exe          ← aplicatia principala
   - gray_writer.exe  ← program intern de scriere in gray_list.txt
   - white_list.txt
   - black_list.txt
   - gray_list.txt
   - folderul /images cu imaginile CarsXXX.png

2. NU este nevoie de instalare sau conexiune la internet.

3. Ruleaza aplicatia:
   - Dublu click pe `app.exe`

4. Vei vedea o interfata cu imaginea curenta si un buton:
   - "Urmatoarea imagine" — avanseaza la urmatoarea imagine din folderul `images`

────────────────────────────────────────────
CE FACE APLICATIA
────────────────────────────────────────────

- Extrage automat textul (numarul de inmatriculare) din fiecare imagine.
- Verifica daca numarul este:
   - ✅ in white list → afiseaza "Permis"
   - ❌ in black list → afiseaza "Interzis"
   - ⚠️ necunoscut   → il adauga in `gray_list.txt`

────────────────────────────────────────────
FISIERE NECESARE IN ACELASI FOLDER
────────────────────────────────────────────

- app.exe
- gray_writer.exe
- white_list.txt
- black_list.txt
- gray_list.txt
- /images/

Toate fisierele trebuie sa fie in acelasi director cu `app.exe`.

────────────────────────────────────────────
COMPATIBILITATE
────────────────────────────────────────────

- Functioneaza pe Windows 10 sau mai nou
- NU necesita instalarea de Python sau alte programe
- Daca Windows Defender blocheaza rularea:
   - Click dreapta > Run anyway (Ruleaza oricum)

────────────────────────────────────────────
SUPORT SI CONTACT
────────────────────────────────────────────

Aceasta aplicatie este creata in scop demonstrativ.  
Pentru intrebari sau sugestii: dragos_stefan.paiu@stud.acs.upb.ro 
