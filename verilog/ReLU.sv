module ReLU(input logic in[15:0], output logic out[15:0]);
    assign out[15:0] = in[15] ? 15'b0 : in[15:0];
endmodule
