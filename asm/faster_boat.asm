push r0, r1, r2, r3, r4, r5 ; preserve original function's register values

; load constant 0xF7FFF5B4 into r0
ldr r0, =0xF7FFF5B4

; get value at memory location 0x20EE4B4 and add r0 (0xF7FFF5B4) to it
ldr r5, =0x20EE4B4
ldr r5, [r5]
add r5, r5, r0

; store 0x8000000 in r1
mov r1, 8
lsl r1, 24

; r2 = current boat speed
ldr r2, [r1, r5]

; check if R button is pressed.
; if not, don't increase boat speed.
@@check_r_button:
ldr r3, =0x4000130
ldrh r3, [r3]
lsr r3, r3, 0x8
and r3, r3, 0x1
cmp r3, 0x0
bne @@check_l_button

; don't increase if it's at max speed
cmp r2, 0x540
bge @@check_l_button

; otherwise, increase the speed by 0x20
add r2, r2, 0x20
str r2, [r1, r5]

; check if L button is pressed.
; if it is, slow down the boat.
@@check_l_button:
ldr r3, =0x4000130
ldrh r3, [r3]
lsr r3, r3, 0x9
and r3, r3, 0x1
cmp r3, 0x0
bne @@return

; don't decrease if speed is zero
cmp r2, 0x0
beq @@return

; otherwise, decrease the speed by 0x20
sub r2, r2, 0x20
str r2, [r1, r5]

@@return:
pop r0, r1, r2, r3, r4, r5 ; restore original function's register values

; END OF ASM CODE

; this code is based on the following action replay code i found on the internet.
; i've added comments and indentations to make it clearer what the AR codes are doing.
// ; if 20EEC6A | 0 == 0
// 920EEC6A 00000000

//     ; if 20EE4B4 != 0
//     620EE4B4 00000000

//         ; load value (b0) at 20EE4B4
//         B20EE4B4 00000000

//         ; Add F7FFF5B4 to offset
//         DC000000 F7FFF5B4

//         ; 16-bit write 0x340 to 8000000 + offset
//         18000000 00000340

//         ; end code
//         D2000000 00000000
