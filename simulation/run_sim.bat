iverilog -g2012 -o mmu_sim ..\tb\mmu_tb.v ..\rtl\mmu.v ..\rtl\tlb.v ..\rtl\ptw.v ..\rtl\perm_check.v
vvp mmu_sim
gtkwave mmu.vcd
