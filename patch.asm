.nds
.arm

.open "overlay_0061.bin", 0x0213DE40

.org 0x3540 + 0x0213DE40
    .area 20h
    hook1:
        push r14
        str r0, [r4, r3, lsl 0x2]
        pop r15
    .endarea

.close


.open "overlay_0000.bin", 0x02077360

.org 0x00071F60 + 0x02077360
    
.org 0x20424 + 0x02077360
    .area 4h
        bl hook1
    .endarea

.close
