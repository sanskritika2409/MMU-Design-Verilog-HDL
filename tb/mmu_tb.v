`timescale 1ns/1ps

module mmu_tb;

reg clk;
reg rst_n;
reg enable;

reg [31:0] va;

reg read;
reg write;


wire [31:0] pa;
wire pf;
wire prot;
wire valid;


mmu dut(

.clk(clk),
.rst_n(rst_n),
.enable(enable),
.virtual_address(va),
.read(read),
.write(write),

.physical_address(pa),
.page_fault(pf),
.protection_fault(prot),
.valid_translation(valid)

);


always #5 clk=~clk;


initial
begin

$dumpfile("mmu.vcd");
$dumpvars(0,mmu_tb);


clk=0;

rst_n=0;

enable=0;


#20;


rst_n=1;

enable=1;


va=32'h12345000;

read=1;

write=0;


#50;


$finish;


end


endmodule