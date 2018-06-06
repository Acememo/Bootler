	   	    list    p=16F877A
	    include "p16F877A.inc"
	    __CONFIG _FOSC_XT & _WDTE_OFF & _PWRTE_OFF & _CP_OFF
conta1	    EQU	    0x20
conta2	    EQU	    0x21
var1	    EQU	    0x22
var2	    EQU	    0x23
var3	    EQU	    0x24
    
	    org	    0x00
	    goto    configura
	    org	    0x04
	    movf    RCREG,0
	    xorlw   0x31
	    btfss   STATUS,Z
	    bsf	    PORTB, RB0
	    xorlw   0x32
	    btfss   STATUS,Z
	    bsf	    PORTB, RB1
	    xorlw   0x33
	    btfss   STATUS,Z
	    bsf	    PORTB, RB2
	    xorlw   0x34
	    btfss   STATUS,Z
	    bcf	    PORTB, RB0
	    xorlw   0x35
	    btfss   STATUS,Z
	    bsf	    PORTB, RB1
	    xorlw   0x36
	    btfss   STATUS,Z
	    bsf	    PORTB, RB2
	    call    enviar
	    movwf   PORTB
	    bcf	    PIR1,5
	    retfie
	    
	

configura   bsf	    STATUS,RP0    ; PASAR AL BANCO 1 
	    movlw   0x01           
	    movwf   TRISA         ; PUERTO A entrada
	    movlw   0x00
	    movwf   TRISB         ; PUERTO B salida
	    bsf	    TXSTA,BRGH
	    bcf	    TXSTA,SYNC
	    bsf	    TXSTA,TXEN
	    movlw   0x04
	    movwf   ADCON1 
	    movlw   .25
	    movwf    SPBRG
	    bsf	    PIE1,RCIE
	    bcf	    STATUS,RP0	  ; PASAR AL BANCO 0
	    bsf	    RCSTA,SPEN
	    bsf	    RCSTA,CREN
	    bsf	    INTCON,GIE
	    bsf	    INTCON,PEIE
	    clrf    PORTB
	    
	    
configura2  movlw   0x54
	    call    enviar
	    movlw   0x81
	    movwf   ADCON0
	    call    inicio
	    movlw   0x4C
	    call    enviar
	    movlw   0x89
	    movwf   ADCON0
	    call    inicio
	    movlw   0x50
	    call    enviar
	    movlw   0x99
	    movwf   ADCON0
	    call    inicio
	    call    retardo2
	    goto    configura2
	    
inicio	    
	    bsf	    ADCON0,2
	    btfsc   ADCON0,2
	    goto    $-.1
	    
	    CLRF    var1
	    CLRF    var2
	    CLRF    var3
	    movf    ADRESH,0
	    movwf   var3
	    call    centenas
	    movlw   0x30
	    ADDWF   var1,1
	    ADDWF   var2,1
	    ADDWF   var3,1
	    
	    movf    var1,0
	    call    enviar
	    movf    var2,0
	    call    enviar
	    movf    var3,0
	    call    enviar
	    movlw   0x0D
	    call    enviar
	    movlw   0x0A
	    call    enviar
	    return
	    

centenas    movlw   .100
	    subwf   var3,1
	    BTFSS   STATUS,Z
	    goto    compara
	    INCF    var1
decenas	    movlw   .10
	    subwf   var3,1
	    BTFSS   STATUS,Z
	    goto    compara2
	    INCF    var2	
	    return

	    
compara	    BTFSC   STATUS,C
	    goto    incremen1
	    movlw   .100
	    ADDWF   var3,1
	    goto    decenas
	    
incremen1   INCF    var1
	    goto    centenas
compara2    BTFSC   STATUS,C
	    goto    incremen2
	    movlw   .10
	    ADDWF   var3,1
	    return
	    
incremen2   INCF    var2
	    goto    decenas
retardo2    movlw   .255
	    movwf   conta2
Bucle2	    movlw   .255
	    movwf   conta1
	    nop
	    decfsz  conta1,1
	    goto    $-.2
	    decfsz  conta2,1
	    goto    Bucle2
	    return
	    
enviar	    
	    movwf   TXREG
	    bsf	    STATUS,RP0
	    btfss   TXSTA,TRMT
	    goto    $-.1
	    bcf	    STATUS,RP0	    
	    return
	    end



	    
