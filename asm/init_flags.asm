; This code will be executed immediately after a save file is loaded.
; Any flags that need to be set in memory can be set here.

push r0, r3, r4 ; preserve original register values

; Set r0 to the offset where flags start. In the vanilla rom, this is 0x21b553c.
; This is likely heap-allocated though, so the offset may change as we make modifications to the rom.
; So, we can't just use a constant. Luckily the link register contains the offset we need at this point,
; though it is offset by 0x30 so we must subtract that first.
sub r4, lr, 0x30

; Set bridge flag
ldr r0, =0x20000
str r0, [r4]

// These don't work yet
// ; Disable intro CG
// ldr r0, =0x80000000
// mov r3, 0x05
// str r0, [r4, r3, lsl 0x2]
// ; 
// ; Disable Tetra "Help Me" CG
// mov r0, 0x1
// mov r3, 0x6
// str r0, [r4, r3, lsl 0x2]
// ; 
// ; Disable Meeting Ciela CG
// mov r0, 0x2
// mov r3, 0xb
// str r0, [r4, r3, lsl 0x2]

// ; Set initial Oshus talk flag
// mov r0, 0x2 ;0x3
// mov r3, 0x6
// str r0, [r4, r3, lsl 0x2]

// ; Set earthquake Ciela dialog flag
// ;ldr r0, =0x40000000
// mov r0, 0x1
// mov r3, 0xa; 0x7
// str r0, [r4, r3, lsl 0x2]

// ; Set ChuChu first encounter flag
// ldr r0, =0xC0000000
// mov r3, 0x7
// str r0, [r4, r3, lsl 0x2]

pop r0, r3, r4 ; restore original register values
