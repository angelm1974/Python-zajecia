Struktura folderów 

pakiet_Mariusza
├── LICENSE
├── README.md
├── example_pkg
│	├──moj_modul1.py
│	├──moj_modul2.py
│   └── __init__.py
└── setup.py

Procedura tworzenia pakietu
1. Utwórz pliki o strukturze jak powyżej
2. w pliku setup.py dodaj kod z Twoimi danymi
3. Wypełnij swoje moduły kodem
4. Sprawdz czy pakiet działa odwołując się do niego z innego pliku (poza pakietem)
5. zainstaluj twine     pip install twine
6. zbuduj instalatora   python setup.py sdist bdist_wheel
7. sprawdź builda       twine check dist/*
8. opublikuj pakiet     twine upload dist/*
9. podczas publikacji jako użytkownika podaj __token__
10. Hasło jest = wartości tokena