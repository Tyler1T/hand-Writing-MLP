module RNE16(input logic[18:0] big,
            output logic [15:0] rounded);

    assign rounded[15:1] = big[18:3];
    assign rounded[0] = (big[2] & big[1]) | (big[1]&big[0]);

endmodule
