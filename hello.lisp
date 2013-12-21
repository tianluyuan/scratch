;; This buffer contains some functions written for the purposes of learning lisp

(atom ())
(listp '())
(listp (cdr '(a b c)))
(/ 3.0 5.0)
(car '('(a b) '(c d)))

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

(insertR 'd 'b '(a b c))

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
