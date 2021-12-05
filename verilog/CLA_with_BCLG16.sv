module CLA_with_BCLG16(input logic A[15:0], B[15:0], Cin, output logic S[15:0], C);
  wire c8, prop;
  wire [1:0] Gout, Pout;
  CLA_with_BCLG8 s0(A[7:0], B[7:0], Cin, S[7:0], Gout[0], Pout[0]);
  CLA_with_BCLG8 s1(A[15:8], B[15:8], c8, S[15:8], Gout[1], Pout[1]);
  BCLG b0(Gout, Pout, Cin, c8, C, prop);
endmodule
