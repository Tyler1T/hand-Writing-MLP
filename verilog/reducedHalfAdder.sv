module reducedHalfAdder(input logic A, B, output logic S, G, P);
  assign G = A & B;
  assign P = A | B;
  assign S = (A | B) & ~(A & B);
endmodule
