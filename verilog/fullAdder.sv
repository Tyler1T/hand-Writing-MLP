module fullAdder(output logic Cout, S, input logic A, B , Cin);
  wire toOr1, toOr2, aNext;
  halfAdder first(toOr1, aNext, A, B);
  halfAdder second(toOr2, S, aNext, Cin);
  assign Cout = toOr1 | toOr2;
endmodule
