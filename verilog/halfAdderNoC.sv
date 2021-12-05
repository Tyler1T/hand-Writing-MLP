module halfAdderNoC(input logic A, B, output logic S);
  wire n;
  assign Cout = A & B;
  assign n = A & B;
  assign S = (A | B) & ~n;
endmodule
