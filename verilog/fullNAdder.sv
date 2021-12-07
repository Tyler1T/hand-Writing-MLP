module fullNAdder(output logic Cout, S, input logic A, B , Cin);
  wire toOr1, toOr2, aNext, notS;
  halfAdder first(toOr1, aNext, A, B);
  halfAdder second(toOr2, notS, aNext, Cin);
  assign Cout = toOr1 | toOr2;
  assign S = ~notS;
endmodule
