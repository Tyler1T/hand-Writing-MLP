module stimulus();

  logic [0:15] data [783:0];
  logic [0:15] result[9:0];

  logic clk;

  //for five vector numbers we need 3 bits
  logic [31:0] vectornum, errors;

  //the testvector file should be 784 rows each 16 bits wide
  logic [15:0] testVector[783:0];


  // Instantiate DUT
  csam dut(data, result);
  always
    begin
      clk = 1; #5;
      clk = 0; #5;
    end

  initial
    begin
      $readmemb("input0.dat", testVector);
      vectornum = 0; errors = 0;
    end

  always @(posedge clk)
    begin

      {data, result} = testVector[vectornum];
    end

  always @(negedge clk)
    begin
      $display("Outputs = %b ", result);
      $display("");
    end
  end
endmodule
