;; introduksjon til Elisp

(defun multiply-by-seven (number)
  "simple example"
  (interactive "p")
  (message "the result is %d" (* 7 number)))

;; men denne trenger et prefiksargument om man påkaller funksjonen fra M-x

(multiply-by-seven 7)

