
;; Simple program in common lisp

;; en setning inneholder et substantivfrase og et verbfrase

(defun sentence ()
  (append (noun-phrase)
	  (verb-phrase)))

;; en substantivfrase inneholder en bestemt artikkel og et substantiv

;; (defun noun-phrase ()
;;   (append (article)
;; 	  (noun)))

(defun noun-phrase ()
  (append (article)
	  (adj*)
	  (noun)
	  (pp*)))

(defun verb-phrase ()
  (append (verb)
	  (noun-phrase)))

(defun article ()
  (one-of '(the a)))

(defun noun ()
  (one-of '(man ball woman table)))

(defun verb ()
  (one-of '(hit took saw like)))

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

;; Funksjonen "trace" brukes til "debugging", den viser hvordan de ulike
;; funksjonene tar argumenter og skriver ut når de påkalles.

;; "Kleene star" ("clean-E"): ingen eller flere repetisjoner

;; Funksjonen "assoc" tar en nøkkel og en liste med lister og gir tilbake
;; den første listen som starter med den angitte nøkkelen.

(defun adj* ()
  (if (= (random 2) 0)
      nil
      (append (adj) (adj*))))

(defun pp* ()
  (if (= (random 2) 0)
      nil
      (append (pp) (pp*))))

(defun pp ()
  (append (prep)
	  (noun-phrase)))

(defun adj ()
  (one-of '(big little blue green adiabatic)))

(defun prep ()
  (one-of '(to in by with on)))

(defparameter *simple-grammar*
  '((sentence -> (noun-phrase verb-phrase))
    (noun-phrase -> (Article Noun))
    (verb-phrase -> (Verb noun-phrase))
    (Article -> the a)
    (Noun -> man ball woman table)
    (Verb -> hit took saw liked))
  "A grammar for a trivial subset of English.")

(defvar *grammar* *simple-grammar*
  "The grammar used by generate.  Initially, this is
  *simple-grammar*, but we can switch to other grammers.")

;;; ==============================

;;; Define how to manipulate this data
;;; Accessors for the Knowledge base.

(defun rule-lhs (rule)
  "The left hand side of a rule."
  (first rule))

(defun rule-rhs (rule)
  "The right hand side of a rule."
  (rest (rest rule)))

(defun rewrites (category)
  "Return a list of the possible rewrites for this category."
  (rule-rhs (assoc category *grammar*)))


;;; ==============================
;;; Use the knowledge base to solve the problem:
;;; 

;;; That's all it takes!
(defun generate (phrase)
  "Generate a random sentence or phrase"
  (cond ((listp phrase)
         (mappend #'generate phrase))
        ((rewrites phrase)
         (generate (random-elt (rewrites phrase))))
        (t (list phrase))))
