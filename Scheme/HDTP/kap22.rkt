;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname kap22) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))


(define (add x)
  (local ((define (x-adder y)
            (+ x y)))
    x-adder))

;Denne her forstår jeg lite av, define knytter f til
;(add 5) som er x-adder og som tar et parameter, men
;definisjonen mangler et parameter gjør den ikke?

(define f (add 5))