# Automatic-number-plate-recognition
Acesta este un proiect simplificat de recunoaștere automată a numerelor de înmatriculare (ANPR), care procesează imagini pentru a extrage și clasifica plăcuțele în funcție de liste predefinite: white list, black list și gray list. Proiectul folosește OCR pentru recunoașterea caracterelor și permite extinderea către aplicații precum parcări inteligente, control acces, sau sisteme de securitate.

# Funcționalități
OCR pe imagini cu plăcuțe auto folosind EasyOCR

Comparare fuzzy cu liste de referință (white/black list) prin RapidFuzz

Trimiterea numerelor necunoscute către o listă intermediară (gray list)

Suport pentru procesarea în batch a imaginilor dintr-un folder

# Structură generală
Proiectul face referire la câteva fișiere și directoare care nu sunt incluse în acest repository și trebuie adăugate manual:

images/ – folder ce conține imaginile de intrare (numele fișierelor trebuie să înceapă cu Cars și să aibă extensia .png)

white_list.txt – listă cu numere de înmatriculare autorizate

black_list.txt – listă cu numere blocate/ignorate

gray_list.txt – listă unde se adaugă automat numerele necunoscute

gray_writer.exe – executabil extern care primește ca argument un număr necunoscut și îl scrie în gray_list.txt

⚠️ Notă importantă
Baza de date (imagini) și listele white_list.txt / black_list.txt / gray_list.txt NU sunt incluse în acest repository.
Utilizatorul este responsabil să le creeze sau să le obțină. Formatul este simplu, cu un număr de înmatriculare pe fiecare linie.

📝 Observații
OCR-ul se face pe o versiune inversată (negative) a imaginii pentru rezultate mai bune.

Codul acceptă doar fișiere care încep cu Cars și se termină în .png.

Similaritatea este verificată cu un prag de 70% (poți ajusta).

Dacă un număr nu se regăsește în nicio listă, este trimis către gray_writer.exe, care îl va adăuga în gray_list.txt.
