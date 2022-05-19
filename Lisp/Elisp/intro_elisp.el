;; introduksjon til Elisp

(defun multiply-by-seven (number)
  "eksempel på funksjonsdefinisjon
   anger et tall med syv"
  (interactive "p")  ; "p" står for prefix argument
  (message "the result is %d" (* 7 number)))

;; men denne trenger et prefiksargument om man påkaller funksjonen fra M-x

(multiply-by-seven 7)

(let ((zebra "stripes") ;; varlist
      (tiger "fierce")) 
  (message "One kind of animal has %s and another is %s."
	   zebra tiger)) ;; body

(defun type-of-animal (characteristics)
  "determines which characteristics"
  (if (equal characteristics "fierce")
      (message "It is a tiger")
    (message "It is not fierce")))

(type-of-animal "fierce")
(type-of-animal "striped")
