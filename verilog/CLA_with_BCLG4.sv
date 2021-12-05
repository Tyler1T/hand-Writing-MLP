module CLA_with_BCLG4(input logic A[3:0], B[3:0], Cin, output logic S[3:0], G, P);
  wire c2;
  wire [1:0] Gout, Pout;
  CLA_with_BCLG2 s0(A[1:0], B[1:0], Cin, S[1:0], Gout[0], Pout[0]);
  CLA_with_BCLG2 s1(A[3:2], B[3:2], c2, S[3:2], Gout[1], Pout[1]);
  BCLG b0(Gout, Pout, Cin, c2, G, P);
endmodule
