;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname kap19) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;similarities in definitions

; contains-doll?: los -> boolean
(define (contains-doll? alos)
  (cond
    [(empty? alos) false]
    [else
     (cond
       [(symbol=? (first alos) 'doll) true]
       [else (contains-doll? (rest alos))])]))

; contains-car?: los -> boolean
(define (contains-car? alos)
  (cond
    [(empty? alos) false]
    [else
     (cond
      [(symbol=? (first alos) 'car) true]
      [else (contains-car? (rest alos))])]))

;strukturen på begge disse funksjonene er i prinsippet identisk
;en generalisering av funksjonene ville være fornuftig, og i denne
;generaliseringen så ser vi det at antallet parametre som funksjonen
;tar vokser med en
;navnet på denne teknikken er FUNCTIONAL ABSTRACTION

(define (contains? something alos)
  (cond
    [(empty? alos) false]
    [else
     (cond
       [(symbol=? (first alos) something) true]
       [else (contains? something (rest alos))])]))

; below: lon number -> lon
(define (below alon t)
  (cond
    [(empty? alon) empty]
    [else
     (cond
       [(< (first alon) t) (cons (first alon) (below (rest alon) t))]
       [else (below (rest alon) t)])]))

; above: lon number -> lon
(define (above alon t)
  (cond
    [(empty? alon) empty]
    [else
     (cond
       [(> (first alon) t) (cons (first alon) (above (rest alon) t))]
       [else (above (rest alon) t)])]))

; filter1: relasjon alon t
(define (filter1 relasjon alon t)
  (cond
    [(empty? alon) empty]
    [else
     (cond
       [(relasjon (first alon) t) (cons (first alon) (filter1 relasjon (rest alon) t))]
       [else (filter1 relasjon (rest alon) t)])]))