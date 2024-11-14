# Algorytm Smitha-Watermana

Algorytm Smitha-Watermana wykorzystywany jest do lokalnego dopasowania dwóch sekwencji metodą programowania dynamicznego. Polega na stworzeniu i uzupełnieniu macierzy o n+1 kolumnach i m+1 wierszach, gdzie n i m to długości sekwencji, a następnie wykonaniu backtrackingu. Jest odpowiedni do porównywania sekwencji mających różną długość i pochodzenie, ponieważ nie musimy w nim uwzględniać całych sekwencji.

## Działanie programu

**Dane wejściowe**
- plik FASTA z rozszerzeniem *.fa* zawierający dwie sekwencje aminokwasowe wraz z nagłówkami (identyfikatorami)
- wartość match
- wartość mismatch
- wartość gap
  
**Dane wyjścowe**
- plik z rozszerzeniem *.txt* zawierający dopasowanie sekwencji oraz score dla tego dopasowania

Komórki macierzy wypełniamy zgodnie ze wzorem:
M[i,j] = max{M[i-1,j-1] + s(i,j), M[i-1,j] + g, M[i,j-1] + g, 0} 

## Sposób użycia 

1. Zapisz w pliku *para_sekwencji.fa* dwie sekwencje, które mają zostać dopasowane wraz z nagłówkami zaczynającycmi się od znaku ">"
2. Uruchom program w terminalu
3. Jeśli zawartość pliku jest prawidłowa, program poprosi o wprowadzenie wartości dla parametrów *match, mismatch, gap* (podane wartości są zaokrąglane do liczb całkowitych)
5. Program dopasowuje sekwencje za pomocą zaimplementowaego algorytmu Smitha-Watermana
6. Dopasowanie sekwencji oraz *score* dla dopasowania zapisane zostaną w pliku tekstowym *sw.txt*

## Przykładowe użycie

**Zawartość pliku wejściowego**
```
>2HHB_1|Chains A, C|HEMOGLOBIN (DEOXY) (ALPHA CHAIN)|Homo sapiens (9606)
VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR
>2HHB_2|Chains B, D|HEMOGLOBIN (DEOXY) (BETA CHAIN)|Homo sapiens (9606)
VHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH
```

**Uruchomienie programu**
```
python smith-waterman.py para_sekwencji.fa
```

**Wprowadzenie wartości parametrów**
```
Wprowadz wartosc dla match (podana wartosc zostanie zaokraglona do l.calkowitej): 1
Wprowadz wartosc dla mismatch (podana wartosc zostanie zaokraglona do l.calkowitej): -1
Wprowadz wartosc dla gap (podana wartosc zostanie zaokraglona do l.calkowitej): 0
```

**Zawartość pliku wyjściowego**
```
s1: V-L-----SPA-DKTNVKA-AWGK-----VGAHAGEYGAEAL-ER-MFL---SFP-T---TKTYF--PHF-DLS------HG---SAQVK-GHGKKV--A--D-ALTNAVAH-VDDMPNAL----SA-LS-DLH--AHKL-RVDP-VNF--KL---L-SHCLLVTLA-AH---LPAEFT-P--AVHA--SLDK--FLA-SV---STVL--TSKY
s2: VHLTPEEKS-AV--T---AL-WGKVNVDEV----G--G-EALG-RL--LVVY--PWTQRF----FES--FGDLSTPDAVM-GNPK---VKA-HGKKVLGAFSDG-L----AHL--D--N-LKGTF-ATLSE-LHCD--KLH-VDPE-NFRL-LGNVLV--C--V-LAH-HFGK---EFTPPVQA--AYQ---KVV--AG-VANA---LAH--KY
score: 71
```
