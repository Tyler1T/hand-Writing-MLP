module stimulus();

  logic [15:0] Y;
  logic [15:0] X;
  logic [15:0] Z;

  logic [15:0] answer;
  logic clk;

  //for five vector numbers we need 3 bits
  logic [31:0] vectornum, errors;

  //the testvector file should be 2 rows each 48 bits wide
  logic [47:0] testVector[1:0];


  // Instantiate DUT
  csam dut(answer, X, Y);
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
