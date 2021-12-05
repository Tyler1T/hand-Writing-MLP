module regfile_bias2(input  logic [5:0] ra1,
                output logic [15:0] rd1);

    // one port register file
    // read one port combinationally
    //ra1 is the address that we want to read
    //rd1 is the data from memory that we get

    logic [15:0] rf[5:0];
    // rf is register file, 15:0 is data size and 14:0 is file length
    initial
        begin
            $readmemb("./bias2.txt", rf1);
        end

   assign rd1 = rf[ra1];

endmodule // regfile
