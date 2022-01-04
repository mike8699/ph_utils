.nds
.relativeinclude on
.erroronwarning on

.open "arm9_original.bin","arm9_compressed.bin",0x02004000

    // .thumb
    // .org 0x2B156 + 0x2004000
    //     ; disable save file checksum verification
    //     .area 0x2
    //         ldr r0, =0x2E24
    //     .endarea
    //     .pool

    .arm
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

            @drop_lookup:
                push lr
                ldr r0, [r4, 0x6C] ; original instruction, don't change
                .include "asm/drop_lookup.asm"
                pop pc
        .pool
        .endarea

.close


.open "overlay/overlay_0000.bin", 0x02077360
    .arm
    .org 0x20300 + 0x02077360
        .area 0x4
            b @init_flags
        .endarea

    .arm
    .org 0x202DC + 0x02077360
        .area 0x4
            bl @set_flags
        .endarea
.close


// .open "overlay/overlay_0022.bin", 0x02112BA0
//     .arm
//     .org 0x4B98 + 0x02112BA0
//         ; patch out savefile checksum verification
//         .area 0x24
//         .endarea
// .close

.open "overlay/overlay_0031.bin", 0x0211F5C0
    .arm
    .org 0x17420 + 0x0211F5C0 ;0x217bce0
        .area 0x4
            bl @faster_boat
        .endarea
.close

.open "overlay/overlay_0037.bin", 0x215b400
    .arm
    ; 0x2162790 in memory
    .org 0x738C + 0x215b400
        .area 0x4
            // bl @drop_lookup
            b 0x2162bf4 ; disables all drops TODO: remove
        .endarea
.close
