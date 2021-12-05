module CLA_with_BCLG8(input logic A[7:0], B[7:0], Cin, output logic S[7:0], G, P);
  wire c4;
  wire [1:0] Gout, Pout;
  CLA_with_BCLG4 s0(A[3:0], B[3:0], Cin, S[3:0], Gout[0], Pout[0]);
  CLA_with_BCLG4 s1(A[7:4], B[7:4], c4, S[7:4], Gout[1], Pout[1]);
  BCLG b0(Gout, Pout, Cin, c4, G, P);
endmodule
