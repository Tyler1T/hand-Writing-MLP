module RCA_GP(input logic A, B, Cin, output logic S, Cout, G, P);
  wire n;
  reducedHalfAdder first(A, B, n, G, P);
  halfAdder second(n, Cin, S, Cout);
endmodule
