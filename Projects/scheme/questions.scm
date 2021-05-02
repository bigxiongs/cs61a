(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
        (cond ((equal? pairs nil) '(nil nil))
              (else (list (cons (caar pairs) (car (zip (cdr pairs)))) (cons (car (cdar pairs)) (cadr (zip (cdr pairs)))))))
)

(zip '((1 2) (3 4) (5 6)))


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (BEGIN
      (define (helpfunc s n)
              (cond ((equal? s nil) nil)
                    (else (cons (cons n (cons (car s) nil)) (helpfunc (cdr s) (+ n 1))))
              ))
      (helpfunc s 0))
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond ((equal? list1 nil) list2)
        ((equal? list2 nil) list1)
        (else
              (if (comp (car list1) (car list2))
                  (cons (car list1) (merge comp (cdr list1) list2))
                  (cons (car list2) (merge comp list1 (cdr list2))))))
  )
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    (begin (if (equal? s nil) nil
           (begin (define (helpfunc s)
                   (cond ((equal? s nil) (list nil s))
                         ((equal? (cdr s) nil) (list s nil))
                         ((< (car (cdr s)) (car s)) (list (cons (car s) nil) (cdr s)))
                         (else (list (cons (car s) (car (helpfunc (cdr s)))) (cadr (helpfunc (cdr s)))))))
           (define get (helpfunc s))
           (define sub (car get))
           (define s (cadr get))
           (cons sub (nondecreaselist s)))))
    )
    ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (let ((formals (car (zip values)))
                 (vals (map let-to-lambda (cadr (zip values)))))
                (cons (quasiquote (lambda (unquote formals) (unquote (let-to-lambda (car body))))) vals))
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           (cons form (cons params (map let-to-lambda body)))
           )
         ; END PROBLEM EC
         )))
   
; test     
(let-to-lambda '(+ 1 (let ((a 1)) a)))



