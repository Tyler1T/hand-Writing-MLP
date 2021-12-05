module ReLU(in, out);
    input logic [15:0] in;
    output logic [15:0] out;

    assign out[15:0] = (in[15] == 0) ? 16'b0 : in[15:0];
endmodule
