module ReLU(in, out);
    input logic [15:0] in;
    output logic [15:0] out;

    logic test;
    assign test = in[15];

    assign out[15:0] = test ? 16'b0 : in[15:0];
endmodule
