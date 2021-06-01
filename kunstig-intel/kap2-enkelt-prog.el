
;; Simple program in common lisp

;; en setning inneholder et substantivfrase og et verbfrase

(defun sentence ()
  (append (noun-phrase)
	  (verb-phrase)))

;; en substantivfrase inneholder en bestemt artikkel og et substantiv

(defun noun-phrase ()
  (append (article)
	  (noun)))

;; en verbfrase inneholder et verb og en substantivfrase

(defun verb-phrase ()
  (append (verb)
	  (noun-phrase)))

;; en artikkel er enten 'a, ubestemt entall, eller 'the, bestemt entall  

(defun article ()
  (one-of '(the a)))

;; et substantiv er enten mann, ball, kvinne eller bord

(defun noun ()
  (one-of '(man ball woman table dog cat squirrel)))

(defun verb ()
  (one-of '(hit took saw liked pushed jumped)))

(defun one-of (set)
  "pick one of set, and make a list of it"
  ;;denne funksjonen sørger kun for at utvalget, som blir gjort
  ;;i funksjonen nedenfor, omgjøres til en liste med ett element
  (list (random-elt set)))


(defun random-elt (choices)
  (elt choices (random (length choices))))

;; (length choices) angir lengden på listen det skal velges fra


;; Funksjonen "elt" plukker et element i fra en liste. Funksjonen tar to
;; argumenter, en liste og posisjonen i listen. Første element starte på 0.

;; Funksjonen "random" tar et argument, ett tall, og den gir tilbake et tall
;; mellom 0 og tallet.
