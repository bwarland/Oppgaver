#lang racket

(define (tallred nummer)
  (+ (quotient nummer 10) (modulo nummer 10)))

(= (tallred 4003) 403)
(= (tallred 403) 43)
