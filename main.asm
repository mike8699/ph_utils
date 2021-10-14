.nds
.relativeinclude on
.erroronwarning on
.arm

.open "arm9_original.bin","arm9_compressed.bin",0x02004000

.org 0x2097664
    .area 0x0
        @function1:
    .endarea

.org 0x54894 + 0x2004000
    .area 0x228, 0xFF
        @set_flags:
            push lr
            mov lr, r0 ; original instruction, do not remove
            pop pc

        @faster_boat:
            push lr
            strlt r0,[r4,0x78] ; original instruction, do not change
            .include "asm/faster_boat.asm"
            pop pc

        @init_flags:
            .include "asm/init_flags.asm"
            pop r3, pc ; original instruction, do not change
    .pool
    .endarea

.close


.open "overlay/overlay_0000.bin", 0x02077360
    .org 0x20300 + 0x02077360
        .area 0x4
            b @init_flags
        .endarea

    .org 0x202DC + 0x02077360
        .area 0x4
            bl @set_flags
        .endarea
.close


.open "overlay/overlay_0031.bin", 0x0211F5C0
    .org 0x17420 + 0x0211F5C0 ;0x217bce0
        .area 0x4
            bl @faster_boat
        .endarea
.close
