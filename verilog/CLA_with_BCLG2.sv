module CLA_with_BCLG2(input logic A[1:0], B[1:0], Cin, output logic S[1:0], G, P);
  wire c1;
  wire [1:0] Gout, Pout;
  reducedFullAdder s0(A[0], B[0], Cin, S[0], Gout[0], Pout[0]);
  reducedFullAdder s1(A[1], B[1], c1, S[1], Gout[1], Pout[1]);
  BCLG b0(Gout, Pout, Cin, c1, G, P);
endmodule
