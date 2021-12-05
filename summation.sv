module summation #(parameter WIDTH=16, parameter LENGTH=50)
   (input  logic [LENGTH-1:0][WIDTH:0] a
    output logic [32:0] y);

    assign y = a.sum() with (a + 0);

endmodule // summation
