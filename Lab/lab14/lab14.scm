(define (split-at lst n)
  (cond ((null? lst) (cons nil nil))
        ((= n 0) (cons nil lst))
        (else (cons (cons (car lst) (car (split-at (cdr lst) (- n 1)))) (cdr (split-at (cdr lst) (- n 1))))))
)


(define (compose-all funcs)
  (define (f x)
          (begin (define (g x funcs)
                         (cond ((null? funcs) x)
                               (else (g ((car funcs) x) (cdr funcs)))))
                 (g x funcs)))
             f)

(define identity (compose-all (list)))
(identity 42)