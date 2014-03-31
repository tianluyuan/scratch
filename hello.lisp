;; This buffer contains some functions written for the purposes of learning lisp
;; To evalulate a line in emacs do C-x C-e and the result will show up in the mini-buffer
;; and the *Messages* buffer

(atom ())
(listp '())
(listp (cdr '(a b c)))
(/ 3.0 5.0)
(car '('(a b) '(c d)))

(defun hello_concat (a)
  (cond
   ((null a) "hello")
   (t (concat  (hello_concat (cdr a)) ", " (car a)))))

(defun hello (a)
  (hello_concat (reverse a)))

(hello '("world" "earth" "universe" "tianlu"))

(defun rem (a lat)
  (cond
   ((null lat) '())
   ((eq a (car lat)) (cdr lat))
   (t (cons (car lat) (rem a (cdr lat))))))

(rem 'and '(bacon lettuce and tomato))

(defun triangle-using-cond (number)
  (cond ((<= number 0) 0)
        ((= number 1) 1)
        ((> number 1)
         (+ number (triangle-using-cond (1- number))))))

(triangle-using-cond 4)

(defun firsts (l)
  (cond
   ((null l) '())
   (t (cons (car (car l)) (firsts (cdr l))))))

(firsts '((a b) (b c) (c d)))

(defun insertR (new old lat)
  (cond
   ((null lat) '())
   ((eq (car lat) old) (cons old (cons new (cdr lat))))
   (t (cons (car lat) (insertR new old (cdr lat))))))

(insertR 'topping 'fudge '(ice cream fudge sundae))

(car (car '((a b) (b c))))
(car '(a b))
(cons '(a b) '())

;; testing recursive addition and multiplication
(defun o+ (n m)
  (cond
   ((zerop m) n)
   (t (1+ (o+ n (1- m))))))

(o+ 5 6)

(defun ox (n m)
  (cond
   ((zerop m) 0)
   (t (o+ n (ox n (1- m))))))

;; lisp default implementations of +/* are not recursive!
(* 100 100)
(ox 100 100)
