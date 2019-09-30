            db      0x7F    ; * id  0                   ; START OF ELF HEADER
            db      0x45    ; * id  1 (E)
            db      0x4C    ; * id  2 (L)
            db      0x46    ; * id  3 (F)
            db      0x58    ; file class            ; pop eax
            db      0x3c    ; data encoding         ; cmp al, 2 (1)
            db      0x02    ; File version          ; cmp al, 2 (2)
jz bridge  ;db      0x74    ; OS/ABI                ; jz short +11 (1)
           ;db      0x0b    ; padding 1             ; jz short +11 (2)
end:        db      0xb3    ; padding 2             ; mov bl, 1 (1)
            db      0x01    ; padding 3             ; mov bl, 1 (2)
            db      0x31    ; padding 4             ; xor eax, eax (1)
            db      0xc0    ; padding 5             ; xor eax, eax (2)
            db      0x40    ; padding 6             ; inc eax
            db      0xcd    ; padding 7             ; int 0x80 (1)
            db      0x80    ; padding 8             ; int 0x80 (2)
            db      0x02    ; * e_type_1
            db      0x00    ; * e_type_2
            db      0x03    ; * e_architecture_1
            db      0x00    ; * e_architecture_2
bridge:     db      0x5e    ; e_version_1           ; pop esi
            db      0x5e    ; e_version_2           ; pop esi
jmp solve  ;db      0xeb    ; e_version_3           ; jmp short +22 (1)
           ;db      0x16    ; e_version_4           ; jmp short +22 (2)
            db      0x04    ; + e_entry_1
            db      0x20    ; + e_entry_2
            db      0x00    ; + e_entry_3
            db      0x01    ; + e_entry_4
            db      0x21    ; + e_progHeaderoff_1
            db      0x00    ; + e_progHeaderoff_2
            db      0x00    ; + e_progHeaderoff_3
            db      0x00    ; + e_progHeaderoff_4
            db      0xff    ; e_sectionHeaderOff_1  ; free byte
            db      0x01    ; e_sectionHeaderOff_2      ; START OF PROGRAM HEADER   ; * p_type_1
            db      0x00    ; e_sectionHeaderOff_3                                  ; * p_type_2
            db      0x00    ; e_sectionHeaderOff_4                                  ; * p_type_3
            db      0x00    ; e_flags_1                                             ; * p_type_4
            db      0x00    ; e_flags_2                                             ; * p_offset_1
            db      0x00    ; e_flags_3                                             ; * p_offset_2
            db      0x00    ; e_flags_4                                             ; * p_offset_3
            db      0x00    ; + e_ehsize_1                                          ; * p_offset_4
            db      0x00    ; + e_ehsize_2                                          ; + p_vaddr_1
            db      0x20    ; + e_phentsize_1                                       ; + p_vaddr_2
            db      0x00    ; + e_phentsize_2                                       ; + p_vaddr_3
            db      0x01    ; * e_phnum_1                                           ; + p_vaddr_4
            db      0x00    ; * e_phnum_2                                           ; p_paddr_1
solve:      db      0x31    ; e_shentsize_1         ; xor edx, edx                  ; p_paddr_2
            db      0xd2    ; e_shentsize_2         ; xor edx, edx                  ; p_paddr_3
            db      0xbd    ; e_shnum_1             ; mov ebp, 0x01002000           ; p_paddr_4
            db      0x00    ; e_shnum_2   c0        ; mov ebp, 0x01002000           ; * p_filesz_1
            db      0x20    ; e_shstrndx_1          ; mov ebp, 0x01002000           ; + p_filesz_2
            db      0x00    ; e_shstrndx_2          ; m ; END OF ELF HEADER         ; p_filesz_3
            db      0x01                            ; mov ebp, 0x01002000           ; p_filesz_4
jmp setret ;db      0x??                            ; jmp short                     ; p_memsz_1
           ;db      0x??                            ; jmp short                     ; p_memsz_2
back: jmp skippf ;db      0x??                            ; jmp short +1 (1)              ; p_memsz_3
           ;db      0x??                            ; jmp short +1 (2)              ; p_memsz_4
            db      0x07                                                            ; * p_flags_1
skippf:     db      0xb8                            ; mov eax, 31                   ; p_flags_2
            db      0x1f                            ; mov eax, 31                   ; p_flags_3
            db      0x00                            ; mov eax, 31                   ; p_flags_4
            db      0x00                            ; mov eax, 31                   ; p_align_1
            db      0x00                            ; mov eax, 31                   ; p_align_2
loop1:      db      0x80                            ; > xorb [esi], 0xdb            ; p_align_3
            db      0x36                            ; > xorb [esi], 0xdb            ; p_align_4
            db      0xdb                            ; > xorb [esi], 0xdb
            db      0x8d                            ; > lea ecx, [ebp+eax+0x61]
            db      0x4c                            ; > lea ecx, [ebp+eax+0x61]
            db      0x05                            ; > lea ecx, [ebp+eax+0x61]
            db      0x61                            ; > lea ecx, [ebp+eax+0x61]
            db      0x31                            ; > xor edx, edx                                
            db      0xd2                            ; > xor edx, edx       
loop2:      db      0x49                            ; >> dec ecx                              
            db      0x02                            ; >> add edx, [ecx]
            db      0x11                            ; >> add edx, [ecx]
            db      0x39                            ; >> cmp ecx, ebp
            db      0xe9                            ; >> cmp ecx, ebp                             
jnz loop2  ;db      0x??                            ; >> jne loop2                                
           ;db      0x??                            ; >> jne loop2                     
            db      0x32                            ; > xor edx, [esi]                         
            db      0x16                            ; > xor edx, [esi]
            db      0x08                            ; > orb [ebp+0xa], dl
            db      0x55                            ; > orb [ebp+0xa], dl                                  
            db      0x0a                            ; > orb [ebp+0xa], dl                                  
            db      0x46                            ; > inc esi
            db      0x48                            ; > dec eax
jns loop1  ;db      0x??                            ; > jno loop1
           ;db      0x??                            ; > jno loop1
jmp end    ;db      0x??                            ; jmp end
           ;db      0x??                            ; jmp end
setret:     db      0x20                            ; and    BYTE PTR [ebp+0xa],dl
            db      0x55                            ; and    BYTE PTR [ebp+0xa],dl
            db      0x0a                            ; and    BYTE PTR [ebp+0xa],dl
jmp back   ;db      0x??                            ; free byte
           ;db      0x??                            ; free byte
            db      0x00                            ; free byte
            db      0xfa                            ; flag byte
            db      0x05                            ; flag byte
            db      0x2a                            ; flag byte
            db      0xd0                            ; flag byte
            db      0x51                            ; flag byte
            db      0xeb                            ; flag byte
            db      0xa6                            ; flag byte
            db      0xbd                            ; flag byte
            db      0x60                            ; flag byte
            db      0x7d                            ; flag byte
            db      0x6d                            ; flag byte
            db      0x01                            ; flag byte
            db      0x25                            ; flag byte
            db      0x13                            ; flag byte
            db      0x67                            ; flag byte
            db      0xbc                            ; flag byte
            db      0xae                            ; flag byte
            db      0xf9                            ; flag byte
            db      0x14                            ; flag byte
            db      0x69                            ; flag byte
            db      0x91                            ; flag byte
            db      0x86                            ; flag byte
            db      0xfc                            ; flag byte
            db      0x06                            ; flag byte
            db      0x2d                            ; flag byte
            db      0xf5                            ; flag byte
            db      0x2f                            ; flag byte
            db      0x6f                            ; flag byte
            db      0x3b                            ; flag byte
            db      0xf3                            ; flag byte
            db      0x75                            ; flag byte
            db      0x7c                            ; flag byte