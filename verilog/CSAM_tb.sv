module stimulus();

  logic [3:0] Y;
  logic [7:0] X;
  logic [11:0] Z;

  logic [11:0] answer;
  logic clk;

  //for five vector numbers we need 3 bits
  logic [31:0] vectornum, errors;

  //the testvector file should be 5 rows each 27 bits wide
  logic [26:0] testVector[5:0];


  // Instantiate DUT
  CSAM2C dut(answer, X, Y);
  always
    begin
      clk = 1; #5;
      clk = 0; #5;
    end

  initial
    begin
      $readmemb("testvector.tv", testVector);
      vectornum = 0; errors = 0;
    end

  always @(posedge clk)
    begin

      {Z, X, Y} = testVector[vectornum];
    end

  always @(negedge clk)
    begin
    if(answer !== Z) begin
      $display("Error: inputs for test X = %b Y = %b", X, Y);
      $display("  outputs = %b (%b expected)", Z, answer);
      $display("");
      errors = errors + 1;
    end

    vectornum = vectornum + 1;
    if(vectornum === 4) begin
      $display("%d tests completed with %d errors", vectornum + 1, errors);
    end
  end
endmodule
