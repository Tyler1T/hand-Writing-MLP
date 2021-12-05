module reducedFullAdder(input logic A, B, C, output logic S, G, P);
  wire n;
  reducedHalfAdder first(A, B, n, G, P);
  halfAdderNoC second(n, C, S);
endmodule
