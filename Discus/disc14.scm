; Write a function that takes a procedure and applies to 
; every element in a given nested list.
; The result should be a nested list with the same structure 
; as the input list, but with each element replaced by 
; the result of applying the procedure to that element.
(define (deep-map fn lst)
        (cond ((null? lst) nil)
              ((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
              (else (cons (car lst) (deep-map fn (cdr lst)))))
)