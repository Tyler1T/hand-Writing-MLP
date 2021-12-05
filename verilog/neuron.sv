module neuron_layer1(data, neuron, out);
    input logic [7:0] neuron;
    input logic [783:0] data[15:0];
    output logic [15:0] out;

    logic [15:0] bias;
    logic [17:0] ra1;
    logic [15:0] weight;
    logic [15:0] sum;
    logic [15:0] temp;

    wire to_ReLU;

    regfile_bias1 bias(neuron, bias);

    for(int i = 0; i < 784; i++){
        assign ra1 = {neuron, i};
        regfile_weight1 weight(ra1, weight);
        csam multiplier(temp, weight, data[i])
        CLA_with_BCLG16 adder(temp, pre, 1'b0, sum);
    }

    CLA_with_BCLG16 adder(sum, bias, 1'b0, to_ReLU);

    ReLU activation(to_ReLU, out);
endmodule // 1st hidden layer neuron, 200 neurons

module neuron_layer2(data, bias, neuron, out);
    input logic [5:0] neuron;
    input logic [199:0] data[15:0];
    input logic [15:0] bias;
    output logic [15:0] out;

    logic [17:0] ra1;
    logic [15:0] weight;
    logic [15:0] sum;
    logic [15:0] temp;

    regfile_bias2 bias(neuron, bias);

    for(int i = 0; i < 768; i++){
        assign ra1 = {neuron, i};
        regfile_weight2 weight(ra1, weight);
        csam multiplier(temp, weight, data[i])
        CLA_with_BCLG16 adder(temp, pre, 1'b0, sum);
    }

    ReLU activation(sum, out);
endmodule // 2nd hidden layer neuron, 50 neurons

module neuron_layer3(data, bias, neuron, out);
    input logic [3:0] neuron;
    input logic [49:0] data[15:0];
    input logic [15:0] bias;
    output logic [15:0] out;

    logic [17:0] ra1;
    logic [15:0] weight;
    logic [15:0] sum;
    logic [15:0] temp;

    regfile_bias3 bias(neuron, bias);

    for(int i = 0; i < 768; i++){
        assign ra1 = {neuron, i};
        regfile_weight3 weight(ra1, weight);
        csam multiplier(temp, weight, data[i])
        CLA_with_BCLG16 adder(temp, pre, 1'b0, out);
    }

endmodule // output layer neuron, 10 neurons
