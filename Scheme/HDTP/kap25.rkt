;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname kap25) (read-case-sensitive #t) (teachpacks ((lib "draw.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "draw.rkt" "teachpack" "htdp")) #f)))
;; kapitell 25 generative recursion
;; også kalt algoritme i denne boken

;Funksjoner:
;1) basert på domenekunnskap
;2) oppbygging av datastrukturer
;3) nedbryting av problem i delproblemer til man finner en triviell løsning (grenseløsning)
;
;rekursiv kontra iterativ

;; ball, en datastruktur
;; (make-ball N N N N) der N er et tall (heltall i dette skriptet)
(define-struct ball (x y delta-x delta-y))

;; move-ball: ball -> ball
;; modellerer en balls bevegelse over kanvas

(define (move-ball a-ball)
  (make-ball (+ (ball-x a-ball)
                (ball-delta-x a-ball))
             (+ (ball-y a-ball)
                (ball-delta-y a-ball))
             (ball-delta-x a-ball)
             (ball-delta-y a-ball)))

;; draw-and-clear: a-ball -> true
;; draw, sleep, clear a disk from the canvas
(define (draw-and-clear a-ball)
  (and
   (draw-solid-disk (make-posn (ball-x a-ball)
                               (ball-y a-ball))
                    5
                    'red)
   (sleep-for-a-while DELAY)
   (clear-solid-disk (make-posn (ball-x a-ball)
                               (ball-y a-ball))
                    5
                    'red)))

;; kanvas
(define WIDTH 100)
(define HEIGHT 100)
(define DELAY 0.1)

;; out-of-bounds? a-ball -> boolean
;; is a ball inside or ouside the canvas

(define (out-of-bounds? a-ball)
  (not
   (and
    (<= 0 (ball-x a-ball) WIDTH)      ;; NB! sammenligning 0 <= ball <= WIDTH
    (<= 0 (ball-y a-ball) HEIGHT))))

;; move-until-out: a-ball -> true
;; modellering av ballens bevegelse over kanvas til den går ut

(define (move-until-out a-ball)
  (cond
    [(out-of-bounds? a-ball) true]
    [else (and
           (draw-and-clear a-ball)
           (move-until-out (move-ball a-ball)))]))