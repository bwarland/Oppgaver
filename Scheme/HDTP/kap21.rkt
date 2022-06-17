;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname kap21) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;abstraksjoner fra eksempler




;build-list: N (N->X) -> (listof X)
;filter: (X->boolean) (listof X) ->(listof X)
;quick-sort: (X X -> boolean) (listof X) (listof X)
;map: (X->Y) (listof X) -> (listof Y)
;andmap: (X->boolean) (listof X) -> boolean
;ormap: (X->boolean) (listof X) ->boolean
;foldr: (X Y -> Y) (listof X) -> Y
;foldl: (X Y -> Y) Y (listof X) -> Y
;assf: (X->boolean) (listof (list X Y))->(list X Y) or false

;; flatten-list: (listof (listof X)) -> (listof X)

(define (flatten-list alon)
  (cond
    [(empty? alon) empty]
    [(not (list? (first alon))) (cons (first alon)
                                      (flatten-list (rest alon)))]
    [else (append (cons (first (first alon))
                        (flatten-list (rest (first alon))))
                  (flatten-list (rest alon)))]))

;(equal? (flatten-list empty) empty)
;(equal? (flatten-list '(1 2 3 4)) '(1 2 3 4))
;(equal? (flatten-list '((1 2 3) (4 5 6))) '(1 2 3 4 5 6))
(equal? (flatten-list '((1 2 3) (4 5) 6)) '(1 2 3 4 5 6))

;; fold

(define (fold func alon)
  (local ((define (list-stop func)
            (cond
              [(equal? func +) 0]
              [(equal? func *) 1]
              [else empty])))
        
    (cond
      [(empty? alon) (list-stop func)]
      ; denne fungerer, men det er noe lite
      ; tilfredstillende med denne løsningen
      [(list? (first alon)) (flatten-list alon)]
      ;=========================================
      [else (func (first alon)
                  (fold func (rest alon)))])))

(equal? (fold * '(1 2 3 4)) 24)
(equal? (fold + '(1 2 3 4)) 10)
(equal? (fold cons '(1 2 3 4)) (list 1 2 3 4))
(equal? (fold cons '((1 2 3) (4 5 6))) '(1 2 3 4 5 6))
             