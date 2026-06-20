module mmu(

input clk,
input rst_n,
input enable,

input [31:0] virtual_address,

input read,
input write,


output reg [31:0] physical_address,

output reg page_fault,

output reg protection_fault,

output reg valid_translation

);


always @(posedge clk)

begin

if(!rst_n)

begin

physical_address<=0;

page_fault<=0;

protection_fault<=0;

valid_translation<=0;

end


else if(enable)

begin

physical_address<=virtual_address;

valid_translation<=1;

page_fault<=0;

protection_fault<=0;

end


end


endmodule