module BCLG(input logic G[1:0], P[1:0], Cin, output logic C1, GG, GP);
  assign C1 = G[0] | (P[0] & Cin);
  assign GG = G[1] | (G[0] & P[1]);
  assign GP = P[1] & P[0];
endmodule
