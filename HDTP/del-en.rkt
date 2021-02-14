;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname del-en) (read-case-sensitive #t) (teachpacks ((lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "draw.rkt" "teachpack" "htdp")) #f)))

;; repetisjon av utvalgte emner
;; sammensatte datastrukturer, hang-man øvelsen og syntaks


;; dist-to-0: aposn -> number
;; tar en et punkt/en posisjon i et koordinatsystem og angir distanse til nullpunkt/origo

(define posn1 (make-posn 3 4))
(define posn2 (make-posn 8 6))
(define posn3 (make-posn 5 12))


(define (dist-to-0 aposn)
  (sqrt (+ (sqr (posn-x aposn))
           (sqr (posn-y aposn)))))

;; (= (dist-to-0 posn1) 5)
;; (= (dist-to-0 posn2) 10)
;; (= (dist-to-0 posn3) 13)


;; dimensjoner trafikklys
(define WIDTH 50)
(define HEIGHT 160)
(define BULB-RADIUS 20)
(define BULB-DISTANCE 10)

;; trafikklysposisjoner
(define X-BULBS (quotient WIDTH 2))
(define Y-RED (+ BULB-DISTANCE BULB-RADIUS))
(define Y-YELLOW (+ Y-RED BULB-DISTANCE (* 2 BULB-RADIUS)))
(define Y-GREEN (+ Y-YELLOW BULB-DISTANCE (* 2 BULB-RADIUS)))

;; tegn trafikklys med rødt lys påslått
;; (start WIDTH HEIGHT)
;; (draw-solid-disk (make-posn X-BULBS Y-RED) BULB-RADIUS 'red)
;; (draw-circle (make-posn X-BULBS Y-YELLOW) BULB-RADIUS 'yellow)
;; (draw-circle (make-posn X-BULBS Y-GREEN) BULB-RADIUS 'green)

;; (define RED-C (draw-circle (make-posn X-BULBS Y-RED) BULB-RADIUS 'red))
;; (define RED-B (draw-solid-disk (make-posn X-BULBS Y-RED) BULB-RADIUS 'red))
;; (define YELLOW-C (draw-circle (make-posn X-BULBS Y-YELLOW) BULB-RADIUS 'yellow))
;; (define YELLOW-B (draw-solid-disk (make-posn X-BULBS Y-YELLOW) BULB-RADIUS 'yellow))
;; (define GREEN-C (draw-circle (make-posn X-BULBS Y-GREEN) BULB-RADIUS 'green))
;; (define GREEN-B (draw-solid-disk (make-posn X-BULBS Y-GREEN) BULB-RADIUS 'green))

;; 6.2.1
;; (start 300 300)
;; (draw-solid-line (make-posn 1 1) (make-posn 25 25) 'red)
;; (draw-solid-rect (make-posn 20 20) 25 200 'blue)
;; (draw-circle (make-posn 200 10) 50 'red)
;; (draw-solid-disk (make-posn 200 10) 50 'green)
;; (stop)

;; https://docs.racket-lang.org/teachpack/draw.html

;; ,----
;; | 6.2.2
;; | clear-bulb: symbol -> true
;; `----
;; funksjon som "slår av" eller visker ut et traffikklys
;; symbol: 'green, 'yellow, 'red


(define (clear-bulb bulb-color)
  (cond
    [(equal? bulb-color 'red) (and (clear-solid-disk (make-posn X-BULBS Y-RED) BULB-RADIUS 'red)
                                   (draw-circle (make-posn X-BULBS Y-RED) BULB-RADIUS 'red))]
    [(equal? bulb-color 'yellow) (and (clear-solid-disk (make-posn X-BULBS Y-YELLOW) BULB-RADIUS 'yellow)
                                      (draw-circle (make-posn X-BULBS Y-YELLOW) BULB-RADIUS 'yellow))]
    [(equal? bulb-color 'green) (and (clear-solid-disk (make-posn X-BULBS Y-GREEN) BULB-RADIUS 'green)
                                     (draw-circle (make-posn X-BULBS Y-GREEN) BULB-RADIUS 'green))]
    [else #f]))


;; ,----
;; | 6.2.3
;; | draw-bulb: symbol -> true
;; `----
;; funksjon som tegner eller slår på et trafikklys
;; symbol: 'green, 'yellow, 'red

;; (define (draw-bulb-v1 bulb-color)
;;   (cond
;;     [(equal? bulb-color 'red) (and (clear-bulb 'yellow)
;;                                    (clear-bulb 'green)
;;                                    (draw-solid-disk (make-posn X-BULBS Y-RED) BULB-RADIUS 'red))]
;;     [(equal? bulb-color 'yellow) (and (clear-bulb 'red)
;;                                       (clear-bulb 'green)
;;                                       (draw-solid-disk (make-posn X-BULBS Y-YELLOW) BULB-RADIUS 'yellow))]
;;     [(equal? bulb-color 'green) (and (clear-bulb 'yellow)
;;                                      (clear-bulb 'red)
;;                                      (draw-solid-disk (make-posn X-BULBS Y-GREEN) BULB-RADIUS 'green))]
;;     [else (and (clear-bulb 'red)
;;                (clear-bulb 'yellow)
;;                (clear-bulb 'green))]))

;; Den første versjonen fungerte fint, men nå kan det være tilfeller der man ønsker å slå på alle lys
;; samtidig og da tror jeg denne funksjonen ikke ville passe inn godt. Derfor lages en versjon to.

(define (draw-bulb-v2 bulb-color)
  (cond
    [(equal? bulb-color 'red) (draw-solid-disk (make-posn X-BULBS Y-RED) BULB-RADIUS 'red)]
    [(equal? bulb-color 'yellow) (draw-solid-disk (make-posn X-BULBS Y-YELLOW) BULB-RADIUS 'yellow)]
    [(equal? bulb-color 'green) (draw-solid-disk (make-posn X-BULBS Y-GREEN) BULB-RADIUS 'green)]
    [else #f]))


;; ,----
;; | 6.2.4
;; | switch: symbol, symbol -> true
;; `----
;; denne funksjon slår av et lys og på et annet, dvs. bytter fra f.eks rødt til gult, gult til grønt etc.
;; symbol: 'green, 'yellow, 'red

(define (switch bulb-old bulb-new)
  (and (clear-bulb bulb-old)
       (draw-bulb-v2 bulb-new)))


;; ,----
;; | 6.2.5
;; | next: symbol -> symbol
;; `----
;; funksjon skifter fra et lys til et annet
;; symbol: 'red, 'yellow, 'green

(define (next current-color)
  (cond
    [(and (symbol=? current-color 'red)
          (switch 'red 'green)) 'green]
    [(and (symbol=? current-color 'green)
          (switch 'green 'yellow)) 'yellow]
    [(and (symbol=? current-color 'yellow)
          (switch 'yellow 'red)) 'red]))


;; 6.7 Ekstraøvelse: Hangman
;; =============================================================

;; ,----
;; | 6.7.1
;; | draw-next-part: symbol -> #true
;; `----
;; tegner neste del av figur
;; symbol: 'right-leg,'left-leg, 'left-arm, 'right-arm, 'body, 'head, 'noose

;; (start 500 750)
;; (define head (draw-circle (make-posn 250 100) 25 'black))
;; (define body (draw-solid-line (make-posn 250 125) (make-posn 250 275) 'black))
;; (define left-arm (draw-solid-line (make-posn 250 150) (make-posn 150 175) 'black))
;; (define right-arm (draw-solid-line (make-posn 250 150) (make-posn 350 175) 'black))
;; (define left-leg (draw-solid-line (make-posn 250 275) (make-posn 200 400) 'black))
;; (define right-leg (draw-solid-line (make-posn 250 275) (make-posn 300 400) 'black))
;; (define noose (and (draw-solid-line (make-posn 0 25) (make-posn 250 25) 'black)
;;                    (draw-solid-line (make-posn 250 25) (make-posn 250 35) 'black)
;;                    (draw-circle (make-posn 250 85) 50 'black)
;;                    ))

(define (draw-next body-part)
  (cond
    [(symbol=? body-part 'noose) (and (draw-solid-line (make-posn 0 25) (make-posn 250 25) 'black)
                                      (draw-solid-line (make-posn 250 25) (make-posn 250 35) 'black)
                                      (draw-circle (make-posn 250 85) 50 'black))]
    [(symbol=? body-part 'head) (draw-circle (make-posn 250 100) 25 'black)]
    [(symbol=? body-part 'body) (draw-solid-line (make-posn 250 125) (make-posn 250 275) 'black)]
    [(symbol=? body-part 'left-arm) (draw-solid-line (make-posn 250 150) (make-posn 150 175) 'black)]
    [(symbol=? body-part 'right-arm) (draw-solid-line (make-posn 250 150) (make-posn 350 175) 'black)]
    [(symbol=? body-part 'left-leg) (draw-solid-line (make-posn 250 275) (make-posn 200 400) 'black)]
    [(symbol=? body-part 'right-leg) (draw-solid-line (make-posn 250 275) (make-posn 300 400) 'black)]
    [else #f]))

;; (draw-next 'noose)
;; (draw-next 'head)
;; (draw-next 'body)
;; (draw-next 'left-arm)
;; (draw-next 'right-arm)
;; (draw-next 'left-leg)
;; (draw-next 'right-leg)

;; ,----
;; | 6.7.2
;; | definisjon av three-letter word-struktur
;; `----
;; tar tre symboler/bokstaver og produserer et ordstruktur

(define-struct word (l1 l2 l3))

;; ,----
;; | 6.7.3
;; | reveal: x2 word-structure 'symbol -> word structure
;; `----
;; tar to ordstrukturer og et symbol 
;; lager et nytt statusord, dvs. så mye av ordet som er gjettet riktig 

(define tea (make-word 't 'e 'a))
(define t_a (make-word 't '_ 'a))
(define __a (make-word '_ '_ 'a))
(define ___ (make-word '_ '_ '_))

(define (reveal chosen status letter)
  (cond
    [(or (and (symbol=? letter (word-l1 chosen))
              (symbol=? letter (word-l1 status)))
         (and (symbol=? letter (word-l2 chosen))
              (symbol=? letter (word-l2 status)))
         (and (symbol=? letter (word-l3 chosen))
              (symbol=? letter (word-l3 status)))) status]
    [(symbol=? letter (word-l1 chosen)) (make-word letter (word-l2 status) (word-l3 status))]
    [(symbol=? letter (word-l2 chosen)) (make-word (word-l1 status) letter (word-l3 status))]
    [(symbol=? letter (word-l3 chosen)) (make-word (word-l1 status) (word-l2 status) letter)]
    [else (make-word '_ '_ '_)]))

;; (equal? (reveal tea t_a 'a) t_a)
;; (equal? (reveal tea ___ 'a) __a)
;; (equal? (reveal tea ___ 'b) ___)
;; (equal? (reveal tea t_a 'e) tea)

;; ,----
;; | 7.1.2
;; | perimeter
;; `----

;; (define (shape-template a-shape)
;;   (cond
;;     [(square? a-shape) ...]
;;     [(circle? a-shape) ...]
;;     [else #f]))

(define-struct circle (posn radius))
(define-struct square (posn length))

(define circle1 (make-circle (make-posn 10 99) 1))
(define square1 (make-square (make-posn 2 20) 35))
(define square2 (make-square (make-posn 20 20) 30))

(define (perimeter a-shape)
  (cond
    [(square? a-shape) (* 4 (square-length a-shape))]
    [(circle? a-shape) (* 2 pi (circle-radius a-shape))]
    [else #f]))

;; (= (perimeter square1) 140)
;; (= (perimeter square2) 120)
;; (= (perimeter circle1) #i6.283185307179586)

;; ,----
;; | 7.1.3
;; | area
;; `----
;; tar sirkel eller firkant og beregner areal

(define (area a-shape)
  (cond
    [(square? a-shape) (sqr (square-length a-shape))]
    [(circle? a-shape) (* (sqr pi)
                          (circle-radius a-shape))]
    [else #f]))

;; (= (area square1) 1225)
;; (= (area square2) 900)
;; (= (area circle1) #i9.869604401089358)

;; ,----
;; | intermezzo: syntaks og semantikk
;; `=================================

;; <def> = (define (<var> <var> ... <var>)
;;           <exp>)
;;        | (define <var> <exp>)
;;        | (define-struct <var0> (<var1> ...  <var-n> ))  ;; primit: constr, selector, predikat

;; <exp> = <var>                                    ;; variabel
;;        | <con>                                   ;; konstant
;;        | (<prm> <exp> ... <exp>)                 ;; primitiv
;;        | (<var> <exp> ... <exp>)                 ;; define definerer en variabel?
;;        | (cond (<exp> <exp> ... <exp> <exp>))
;;        | (cond (<exp> <exp> ... (else <exp>)))
;;        | (and <exp> <exp>)
;;        | (or <exp> <exp>)


;; MOVING PICTURES
;; ===============

;; ,----
;; | 10.3.1
;; `----
;; data definitions class of shapes

;; en form er:
;; 1) en sirkel-struktur (make-sirkel punkt radius farge), eller
;; 2) en rektangel-struktur (make-rektangel punkt bredde høyde farge) 

;; form          posisjon  størrelse  farge
;; ----          --------  ---------  -----
;; sirkel-1      (50,50)   40         rød
;; rektangle-1   (30,20)   5x5        blå
;; rektangle-2   (65,20)   5x5        blå
;; rektangle-3   (40,75)   20x10      rød
;; rektangle-4   (45,35)   10x30      blå
;; lerret                  300x10

(define-struct sirkel (punkt radius farge))
(define-struct rektangel (punkt bredde høyde farge))
(define-struct punkt (x y))
;; -----------------------------------------------------------------
;; (define lerret (start 500 500))
(define sirkel-1 (make-sirkel (make-posn 50 50) 40 'red))
(define rektangel-1 (make-rektangel (make-posn 30 20) 5 5 'blue))
(define rektangel-2 (make-rektangel (make-posn 65 20) 5 5 'blue))
(define rektangel-3 (make-rektangel (make-posn 40 75) 20 10 'blue))
(define rektangel-4 (make-rektangel (make-posn 45 35) 10 30 'blue))
;; -----------------------------------------------------------------
(define (tegn-sirkel en-sirkel)
  (draw-circle (sirkel-punkt en-sirkel)
               (sirkel-radius en-sirkel)
               (sirkel-farge en-sirkel)))

(define (tegn-rektangel et-rektangel)
  (draw-solid-rect (rektangel-punkt et-rektangel)
                   (rektangel-bredde et-rektangel)
                   (rektangel-høyde et-rektangel)
                   (rektangel-farge et-rektangel)))
;; ------------------------------------------------

;; En liste med former er enten
;; 1) tom
;; 2) en list med former der former er
;; ;; a) sirkel-struktur, eller
;; ;; b) rektangel-struktur

(define losh (list sirkel-1
                   rektangel-1
                   rektangel-2
                   rektangel-3
                   rektangel-4))

;; mal for funksjon som gjør noe med en liste med former

;; (define (<funksjon>-liste-med-former en-liste-med-former)
;;   (cond
;;     [(empty? en-liste-med-former) empty]
;;     [(sirkel? (first en-liste-med-former)) ... <<funksjon>>]
;;     [(rektangel? (first en-liste-med-former)) ... <<<funksjon>>>]
;;     [else empty]    

(define (draw-shape a-shape)
  (cond
    [(sirkel? a-shape) (tegn-sirkel a-shape)]
    [(rektangel? a-shape) (tegn-rektangel a-shape)]
    [else #f]))

(define (shape? a-shape)
  (cond
    [(or (sirkel? a-shape)
         (rektangel? a-shape)) #t]
    [else #f]))

;; ,----
;; | 10.3.2
;; `----
;; draw-losh

(define (draw-losh a-losh)
  (cond
    [(empty? a-losh) #t]
    [else (and (draw-shape (first a-losh))
               (draw-losh (rest a-losh)))]))

;; ,----
;; | 10.3.3 
;; `----
;; translate-losh

(define (translate-sirkel delta en-sirkel)
  (cond
    [(sirkel? en-sirkel) (make-sirkel (make-posn (+ (posn-x (sirkel-punkt en-sirkel)) delta)
                                                 (posn-y (sirkel-punkt en-sirkel)))
                                      (sirkel-radius en-sirkel)
                                      (sirkel-farge en-sirkel))]
    [else #f]))
                                      
(define (translate-rektangel delta et-rektangel)
  (cond
    [(rektangel? et-rektangel) (make-rektangel (make-posn (+ (posn-x (rektangel-punkt et-rektangel)) delta)
                                                          (posn-y (rektangel-punkt et-rektangel)))
                                               (rektangel-bredde et-rektangel)
                                               (rektangel-høyde et-rektangel)
                                               (rektangel-farge et-rektangel))]
    [else #f]))

(define (translate-shape delta a-shape)
  (cond
    [(sirkel? a-shape) (translate-sirkel delta a-shape)]
    [(rektangel? a-shape) (translate-rektangel delta a-shape)]
    [else #f]))
   
;; (translate-shape 10 sirkel-1)
;; (translate-shape 10 rektangel-1)
;; (translate-shape 10 rektangel-2)
;; (translate-shape 10 rektangel-3)
;; (translate-shape 10 rektangel-4)

;; (define (translate-losh delta a-losh)
;;   (cond
;;     [(empty? a-losh) empty]
;;     [else (append (list (translate-shape delta (first a-losh)))
;;                   (translate-losh delta (rest a-losh)))]))

(define (translate-losh delta a-losh)
  (cond
    [(empty? a-losh) empty]
    [else (cons (translate-shape delta (first a-losh))
                (translate-losh delta (rest a-losh)))]))

;; ,----
;; | 10.3.4
;; `----
;; clear-losh

;; (clear-circle p r c)
;; (clear-solid-rect ul width height c)

(define (slett-sirkel en-sirkel)
  (clear-circle (sirkel-punkt en-sirkel)
                (sirkel-radius en-sirkel)
                (sirkel-farge en-sirkel)))

(define (slett-rektangel et-rektangel)
  (clear-solid-rect (rektangel-punkt et-rektangel)
                    (rektangel-bredde et-rektangel)
                    (rektangel-høyde et-rektangel)
                    (rektangel-farge et-rektangel)))

(define (clear-shape a-shape)
  (cond
    [(sirkel? a-shape) (slett-sirkel a-shape)]
    [(rektangel? a-shape) (slett-rektangel a-shape)]
    [else #f]))

(define (clear-losh a-losh)
  (cond
    [(empty? a-losh) #t]
    [else (and (clear-shape (first a-losh))
                (clear-losh (rest a-losh)))]))

;; ,----
;; | 10.3.5
;; `----
;; draw-and-clear-picture

;; (sleep-for-a-while s)

(define (draw-and-clear-picture a-losh)
  (and (draw-losh a-losh)
       (sleep-for-a-while 2)
       (clear-losh a-losh)))

;; ,----
;; | 10.3.6
;; `----
;; move-picture

(define (move-picture delta a-losh)
  (and (draw-and-clear-picture a-losh)
       (draw-losh (translate-losh 5 a-losh))))

;; ,----
;; | !: N -> N
;; `----
;; faktorial

(define (! num)
  (cond
    [(= num 0) 1]
    [else (* num (! (sub1 num)))]))

;; ,----
;; | n-choose-m 
;; `----

(define (n-choose-m n m)
  (/ (! n)
     (* (! m) (! (- n m)))))


;; ,----
;; | 12.2 auxiliary functions
;; `----

;; ,----
;; | insert
;; `----

;; (insert 5 empty) -> (cons 5 empty)
;; (insert 5 (cons 100 (cons -10 empty))) -> (cons 100 (cons 5 (cons -10 empty)))

(define (insert number alist)
  (cond
    [(empty? alist) (cons number empty)]
    [(>= number (first alist)) (cons number alist)]
    [(<= number (first alist)) (cons (first alist) (insert number (rest alist)))]))

;; (equal? (insert 5 empty) (cons 5 empty))
;; (equal? (insert 5 (cons 100 (cons -10 empty))) (cons 100 (cons 5 (cons -10 empty))))

;; ,----
;; | 12.2.1 sort
;; `----

(define (sort a-list)
  (cond
    [(empty? a-list) empty]
    [else (insert (first a-list) (sort (rest a-list)))]))

;; (sort (list 1 2 3 2 1))


;; ,----
;; | 12.2.2 search
;; `----

(define (search number alist-of-numbers)
  (cond
    [(empty? alist-of-numbers) #f]
    [else (or (= (first alist-of-numbers) number)
              (search number (rest alist-of-numbers)))]))


(define L1 (list 4 3 2 1))
(define L2 (list 4 1 4 23 5 5643 13 3 556 6))
(define L3 (list 9 8 7 6 5 5 4 3 1))
(define L4 (list 5643 556 23 13 6 5 4 4 3 1))

;; ,----
;; | AUX - remove-n-from-list: N (listof S) -> (listof S)
;; `----

(define (remove-n n alist)
  (cond
    [(= n 0) alist]
    [else (remove-n (- n 1) (rest alist))]))

;; (equal? (remove-n-from-list 1 list1) (list 2 3 4))
;; (equal? (remove-n-from-list 2 list1) (list 3 4))

;; ,----
;; | AUX- remove-n-from-list-back: n alist
;; `----

(define (remove-n-last n alist)
  (cond
    [(or (empty? (rest alist))
         (= n 0)) empty]
    [else (cons (car alist) (remove-n-last (- n 1) (cdr alist)))]))


;; ,----
;; | AUX - pick-n-from-list: N (listof numbers) -> N
;; `----

(define (pick-n-from-list n alist)
  (cond
    [(empty? alist) #false]
    [(= n 1) (first alist)]
    [else (pick-n-from-list (- n 1) (rest alist))]))

;; (equal? (pick-n-from-list 1 list1) 1)
;; (equal? (pick-n-from-list 3 list1) 3)
;; (equal? (pick-n-from-list 9 list3) 1)
;; (pick-n-from-list 1 list1)

;; ,----
;; | AUX - list-half: (listof X) -> N
;; `----

(define (list-half alist)
  (cond
    [(even? (length alist)) (/ (length alist) 2)]
    [else (/ (+ 1 (length alist)) 2)]))

;; ,----
;; | AUX - nth-element: n alist
;; `----

(define (nth-element n alist)
  (cond
    [(empty? alist) empty]
    [(= n 1) (first alist)]
    [else (nth-element (- n 1) (rest alist))]))

;; ,----
;; | search-sorted: N (listof N) -> boolean
;; `----

(define (search-sorted N loN)
  (cond
    [(= N (first loN)) #t]
    [(< N (nth-element (list-half loN) loN)) (search-sorted N (remove-n (list-half loN) loN))]
    [else (search-sorted N (remove-n-last (list-half loN) loN))]))

;; (equal? (search-sorted 3 L1) #true)
;; (equal? (search-sorted 23 L4) #true)
;; (equal? (search-sorted 1 L3) #true)


;; ,----
;; | 12.4.1 arrangements: word -> (listof words)
;; `----


;; a word is either
;; 1) empty
;; 2) (cons letter word) where letter is a letter and
;;    word is a word (list of letters)



(define bil (cons 'b (cons 'i (cons 'l empty))))
(define auto (cons 'a (cons 'u (cons 't (cons 'o empty)))))
(define lego (cons 'l (cons 'e (cons 'g (cons 'o empty)))))

;; ,----
;; | 12.4.2 insert-everywhere/in-all-words: letter word -> (listof words)
;; `----
;; tar en bokstav og et ord (liste med bokstaver) og lager en liste med
;; en liste av bokstaver (en liste med ord)

;; (define (insert-everywhere/in-all-words letter word)
;;   (cond
;;     ... (empty? word) empty ...
;;     ...      ... (cons letter word) ... 
;;     ... else ...



;; (define (insert-everywhere/in-all-words letter word)
;;   (cond
;;     [(empty? word) empty]
;;     [else (

;; (define (insert-everywhere/in-all-words letter word)
;;   (cond
;;     [(empty? word) empty]
;;     [else (append (list letter word)
;;                   (list 
            

;; (define (arrangements a-word)
;;   (cond
;;     [(empty? a-word) empty]
;;     [else (insert-everywhere/in-all/words (first a-word)
;;                                           (arrangements (rest a-word)))]))

