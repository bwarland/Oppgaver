#lang racket

;; Noe som jeg strevde litt med i Python: det å sammenligne
;; element for element i en liste, det vil si første element
;; mot andre element, andre element mot tredje element
;; og her var elementene bokstaver eller karakterer.

;; Dette var bare del av et problem, og problemet her var hvordan
;; man kan lage en form for funksjon som vurderer hvorvidt et ord
;; har alle bokstaver i seg plassert i henhold til rekkefølgen i
;; alfabetet

;; Enkelt nok i Scheme/Racket for tall

;; (< 1 2 3) -> true
;; (< 1 3 2) -> false

;; (< "a" "b" "c") går ikke da operatør bare tar tall

;; Så en form for konvertering vil være nødvendig
;; 1) først fra streng til enkelte karakterer,
;; 2) til eller fra lowcase eller upper case,
;; 3) og så i fra karakter til tall.

;; ,----
;; | 1) fra streng til enkeltstående karakterer
;; `----

;; (define alfabet "abcdefghijklmnopqrstuvwzxy")
;; (string->list alfabet)
;; (map string (string->list alfabet))

;; ,----
;; | 2) fra upper case til lower case, eller omvendt
;; `----

;; (string? "a")    -> true
;; (equal? "a" "a") -> true
;; (equal? "a" "A") -> false
;; (equal? "a" (string-downcase "A")) -> true
;; (equal? "A" (string-upcase "a"))  -> true

;; ,----
;; | 3) fra karakterer til tall
;; `----

;; (map char->integer (string->list alfabet))
