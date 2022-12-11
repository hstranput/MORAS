@i
M = 0

(LOOP_START)
    
    @i
    A = M
    D = M
    
    @max
    M = D
    
    (SMALL_LOOP)
    @i
    D = M

    @4
    D = A - D
    
    @LOOP_END
    D; JLE
    
    

    @max
    D = M
    
    @i
    M = M + 1
    A = M
    D = M - D
    
    
    

    @LOOP_START
    D; JGT
    
    @SMALL_LOOP
    0; JMP
    
(LOOP_END)

@max
D = M

@R5
M = D

(END)
@END
0; JMP